import os
import cPickle
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

traindata = []
trainlabel = []

f = file('InputSentenceVectors.save', 'rb')
traindata = cPickle.load(f)
f.close()

f = file('InputSentenceVectors_Labels.save', 'rb')
trainlabel = cPickle.load(f)
f.close()

alldata = ClassificationDataSet(100, 1, nb_classes=2)

for i in xrange(len(traindata[:546])):
	alldata.addSample(traindata[i], trainlabel[i])

tstdata_temp, trndata_temp = alldata.splitWithProportion(0.1)

tstdata = ClassificationDataSet(100, 1, nb_classes=2)
for n in xrange(0, tstdata_temp.getLength()):
	tstdata.addSample( tstdata_temp.getSample(n)[0], tstdata_temp.getSample(n)[1] )

trndata = ClassificationDataSet(100, 1, nb_classes=2)
for n in xrange(0, trndata_temp.getLength()):
	trndata.addSample( trndata_temp.getSample(n)[0], trndata_temp.getSample(n)[1] )

trndata._convertToOneOfMany( )
tstdata._convertToOneOfMany( )

print "Number of training patterns: ", len(trndata)
print "Number of training patterns: ", len(tstdata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]

if  os.path.isfile('capstone.xml'): 
	fnn = NetworkReader.readFrom('capstone.xml') 
else:
	fnn = buildNetwork( trndata.indim, 50 , trndata.outdim, outclass=SoftmaxLayer )

trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

trainer.trainUntilConvergence(trndata, maxEpochs=200, verbose=True, continueEpochs=10, validationProportion=0.1)
'''
for i in range(200):
	trainer.trainEpochs(1)
	trnresult = percentError(trainer.testOnClassData(), trndata['class'])
	tstresult = percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])

	print "epoch: %4d" % trainer.totalepochs, \
		  "  train error: %5.2f%%" % trnresult, \
		  "  test error: %5.2f%%" % tstresult
'''
NetworkWriter.writeToFile(fnn, 'capstone.xml')

'''
f = file('TestSentenceVectors.save', 'rb')
actualtestdata = cPickle.load(f)
f.close()
'''
acttestdata = ClassificationDataSet(100, 1, nb_classes=2)
for i in xrange(len(traindata)):
	acttestdata.addSample(traindata[i], 0)

result = []
p = fnn.activateOnDataset(acttestdata)
print type(p)
f = file('NNProb.save', 'wb')
cPickle.dump(p, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()

for out in p:
	if out[0] > out[1]:
		result.append(0)
	else:
		result.append(1)

with open('CapstoneResultNN.txt', 'w') as f:
	for x in result:
		f.write('%s\n' % x)