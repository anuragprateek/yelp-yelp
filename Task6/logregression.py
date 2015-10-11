import cPickle
import pandas
# Import the linear regression class
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
# Sklearn also has a helper that makes it easy to do cross validation
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
import numpy as np
from sklearn import svm

# Initialize the algorithm class
alg = LogisticRegression(penalty='l1', random_state=1)
#alg = svm.SVC()

#alg = RandomForestClassifier(n_jobs=1)

trainlabel = []

f = file('NNProb.save', 'rb')
traindata = cPickle.load(f)
f.close()
#print traindata

f = file('InputSentenceVectors_Labels.save', 'rb')
trainlabel = cPickle.load(f)
f.close()
#print trainlabel
X = traindata[:546]

print X
print type(X)
print X.shape


numofreviews = []

with open('NumOfReviews.txt', 'r') as f:
	lines = f.readlines()
	for l in lines:
		l.strip()
		numofreviews.append(int(l[0]))

nor_tr = np.array(numofreviews[:546]).reshape(546,1)
nor_tst = np.array(numofreviews[546:]).reshape(12753, 1)

X = np.hstack((X, nor_tr))
print X.shape

avgrating = []

with open('AvgRating.txt', 'r') as f:
	lines = f.readlines()
	for l in lines:
		l.strip()
		avgrating.append(int(l[0]))

avgr_tr = np.array(avgrating[:546]).reshape(546, 1)
avgr_tst = np.array(avgrating[546:]).reshape(12753, 1)

X = np.hstack((X, avgr_tr))

print "Reading cuisines offered ..."
cuisineoffered1 = []
cuisineoffered2 = []

f = file('CuisinesOffered1.save', 'rb')
cuisineoffered1 = cPickle.load(f)
f.close()

f = file('CuisinesOffered2.save', 'rb')
cuisineoffered2 = cPickle.load(f)
f.close()

cuio_tr = np.array(cuisineoffered1[:546]).reshape(546, 1)
cuio_tst = np.array(cuisineoffered1[546:]).reshape(12753, 1)
cuio2_tr = np.array(cuisineoffered2[:546]).reshape(546, 1)
cuio2_tst = np.array(cuisineoffered2[546:]).reshape(12753, 1)

X = np.hstack((X, cuio_tr))
X = np.hstack((X, cuio2_tr))


print X.shape
y = np.array(trainlabel)

print y.shape

alg.fit(X, y)
print alg.score(X, y)

scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=3)
print scores
print scores.mean()

'''
f = file('TestSentenceVectors.save', 'rb')
actualtestdata = cPickle.load(f)
f.close()

Xt = np.array(actualtestdata[0])
for x in actualtestdata[1:]:
	Xt = np.vstack((Xt, x))
'''
Xt = traindata[546:]
Xt = np.hstack((Xt, avgr_tst))
Xt = np.hstack((Xt, cuio_tst))
Xt = np.hstack((Xt, cuio2_tst))

pred = alg.predict(Xt)

print type(pred), pred.shape
with open('CapstoneLogReg2.txt', 'w') as f:
	for y in pred:
		f.write('%s\n' %y)