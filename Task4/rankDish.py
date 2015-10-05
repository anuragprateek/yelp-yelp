'''
head = []
N = 6
with open("sentimentIndian.txt") as myfile:
	head = [next(myfile) for x in xrange(N)]

print head
'''
import csv

reviews=[]
scores=[]
ratings=[]
with open('elrond.txt','r') as f:
	reader=csv.reader(f,delimiter='\t')
	for review,score,rating in reader:
		reviews.append(review.lower())
		scores.append(float(score))
		ratings.append(rating)

#print(reviews)
#print(scores)
#print(ratings)

# Dishes to look for.
dishesToRank = {}
dishesToRankCount = {}
with open('dishrank.txt', 'r') as f:
	dishesToRank = {next(f).rstrip('\n') : 0 for x in xrange(40)}
	
with open('dishrank.txt', 'r') as f:
	dishesToRankCount = {next(f).rstrip('\n') : 0 for x in xrange(40)}

# Read each line, check for bigrams and trigrams that match with dishesToRank, and add score.

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return set([ ' '.join(grams) for grams in n_grams])

for i in range(len(reviews)):
	if scores[i] > 2:
		bigrams = get_ngrams(reviews[i], 2)
		for bg in bigrams:
			if bg in dishesToRank:
				dishesToRank[bg] += scores[i] - 2
				dishesToRankCount[bg] += 1
				if bg == 'masala dosa':
					print 'score for dosa ' + str(dishesToRank[bg])
					print 'count ' + str(dishesToRankCount[bg])
		trigrams = get_ngrams(reviews[i], 3)
		for tg in trigrams:
			if tg in dishesToRank:
				dishesToRank[tg] += scores[i] - 2
				dishesToRankCount[tg] += 1

print dishesToRank
print dishesToRankCount

#for k, v in dishesToRank.iteritems():
#	dishesToRank[k] = dishesToRank[k]/dishesToRankCount[k]

with open('a.txt', 'w') as f:
    f.writelines('{}:{}\n'.format(k,v) for k, v in dishesToRank.items())