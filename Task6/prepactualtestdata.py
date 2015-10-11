vocabsize = 0
inputdim = 0

vocab = {}

print "Reading vocab ..."
with open('vec.txt', 'r') as f:
	line = f.readline().strip()
	line = line.split()
	vocabsize = int(line[0])
	inputdim = int(line[1])
	print vocabsize, inputdim
	lines = f.readlines()
	for l in lines:
		l = l.strip()
		l = l.split()
		vocab[l[0]] = [float(x) for x in l[1:]]

print "Reading training data ..."

traindata = []
notinvocabcnt = 0

linecnt = 0
with open('cleanedinput.dat', 'r') as f:
	for line in f:
		linecnt += 1
		print linecnt
		line = line.strip()
		line = line.split()
		linevec = []
		for word in line:
			if word not in vocab:
				notinvocabcnt += 1
				vocab[word] = [0 for x in xrange(100)]
			if len(linevec) == 0:
				linevec = vocab[word]
			else:
				linevec = map(sum, zip(linevec,vocab[word]))
		linevec = [x/len(line) for x in linevec]
		traindata.append(linevec)
	#print traindata
print str(notinvocabcnt) + ' words not in vocab. '
print len(traindata)
traindata = traindata[546:]
print len(traindata)

import cPickle
f = file('TestSentenceVectors.save', 'wb')
cPickle.dump(traindata, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()