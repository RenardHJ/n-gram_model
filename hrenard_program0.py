import sys
import re
import numpy
from itertools import islice

class ngram:
	def __init__(self, txt, count):
		corpus = re.findall('\w+', txt)
		# text : count
		self.unigramModel = list(corpus)
		self.bigramModel = list(zip(corpus, corpus[1:]))
		self.trigramModel = list(zip(corpus, corpus[1:], corpus[2:]))

		self.count = count

	def unigram(self):
		#randomly selects a word from corpus.
		output = []
		for i in range(self.count):
			output.append(numpy.random.choice(self.unigramModel))
		output = ' '.join(output).capitalize()
		output = output + '.'
		print(output)

	def bigram(self):
		# selects a word based off of the previous word.
		pass

	def trigram(aelf):
		# selects a word based off of the previous two words.
		pass

def main():
	# default settings
	fileName = 'corpus.txt'
	generatedWordCount = 100
	
	# Reading in lines from file
	f = open(fileName, 'r')
	fileOutput = f.read()
	
	# Cleaning file - removing special characters and lower casing all characters
	cleanFileOutput = re.sub(r'[^a-zA-Z0-9]+', ' ', fileOutput).lower()

	#ngram generation
	ng = ngram(cleanFileOutput, generatedWordCount)

	#unigram
	print("Unigram:")
	ng.unigram()

	#bigram
	print("\nBigram:")
	ng.bigram()

	#trigram
	print("\nTrigram:")
	ng.trigram()
main()
