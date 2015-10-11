import string
import nltk
from nltk.corpus import stopwords

exclude = set(string.punctuation)
sw = set(stopwords.words('english'))

print sw

print exclude

with open('cleanedinput.dat', 'w') as f:
	cnt = 0
	for l in open('Hygiene/hygiene.dat', 'r').readlines():
		print cnt
		cnt += 1
		tokens = nltk.word_tokenize(l)
		for token in tokens:
			token = ''.join(ch for ch in token if ch not in exclude)
			token = token.lower();
			if token not in sw:
				f.write(token.lower()+' ')
		f.write('\n')	