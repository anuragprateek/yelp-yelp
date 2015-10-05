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

allrestRating = {}
restRating = {}
restaurants = [line.strip() for line in open('ReviewRest.txt', 'r')]

for i in range(len(reviews)):
	if scores[i] > 2:
		if restaurants[i] in allrestRating:
			allrestRating[restaurants[i]] += scores[i]
		else:
			allrestRating[restaurants[i]] = scores[i]

with open('restaurantsRating.txt', 'w') as f:
    f.writelines('{}:{}\n'.format(k,v) for k, v in allrestRating.items())

top5dishes = ['chicken tikka', 'garlic naan', 'chicken tikka masala', 'tandoori chicken', 'butter chicken']

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
			if bg in top5dishes:
				if restaurants[i] in restRating:
					restRating[restaurants[i]] += scores[i] - 2
				else:
					restRating[restaurants[i]] = scores[i] - 2 
		trigrams = get_ngrams(reviews[i], 3)
		for tg in trigrams:
			if tg in top5dishes:
				if restaurants[i] in restRating:
					restRating[restaurants[i]] += scores[i]
				else:
					restRating[restaurants[i]] = scores[i]

with open('top5dishesRest.txt', 'w') as f:
	f.writelines('{}:{}\n'.format(k,v) for k, v in restRating.items())	