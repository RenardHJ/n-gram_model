import sys
import re
import numpy

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
		
		output = ' '.join(output).capitalize() + '.'
		
		return(output)

	def bigram(self):
		# selects a word based off of the previous word.
		output = []

		prevWord = numpy.random.choice(self.unigramModel)
		output.append(prevWord)

		for i in range(self.count -1):
			prevWord = numpy.random.choice([e[1] for e in self.bigramModel if e[0] == prevWord])
			output.append(prevWord)

		output = ' '.join(output).capitalize() + '.'
		
		return(output)

	def trigram(self):
		# selects a word based off of the previous two words.
		output = []

		prevWord = numpy.random.choice(self.unigramModel)
		prevWord2 = numpy.random.choice([e[1] for e in self.bigramModel if e[0] == prevWord])
		output.append(prevWord)
		output.append(prevWord2)
		
		#print([e[2] for e in self.trigramModel if e[0] == prevWord and e[1] == prevWord2])

		for i in range(self.count - 2):
			temp = prevWord2
			prevWord2 = numpy.random.choice([e[2] for e in self.trigramModel if e[0] == prevWord and e[1] == prevWord2])
			prevWord = temp
			output.append(prevWord2)

		output = ' '.join(output).capitalize() + '.'
		
		return(output)

def main():
	# Default settings
	fileName = 'corpus.txt'
	generatedWordCount = 100
	
	# Reading in lines from file
	f = open(fileName, 'r')
	fileOutput = f.read()
	
	# Cleaning file - removing special characters and lower casing all characters
	cleanFileOutput = re.sub(r'[^a-zA-Z0-9\']+', ' ', fileOutput).lower()

	# Generating ngram models
	ng = ngram(cleanFileOutput, generatedWordCount)

	# Unigram
	print("Unigram:")
	print(ng.unigram())

	# Bigram
	print("\nBigram:")
	print(ng.bigram())

	# Trigram
	print("\nTrigram:")
	print(ng.trigram())

main()
