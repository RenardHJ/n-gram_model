import sys
import re

class ngram:
	def __init__(self, txt):
		self.unigramModel = []
		self.bigramModel = []
		self.trigramModel = []

	def unigram(self):
		pass

	def bigram(self):
		pass

	def trigram(aelf):
		pass

def main():
	# Default settings
	fileName = "corpus.txt"
	nValue = 3
	generatedWordCount = 100
	
	# Reading in lines from file
	f = open(fileName, "r")
	fileOutput = f.read()
	
	# Cleaning file - removing special characters and lower casing all characters
	cleanFileOutput = re.sub(r"[^a-zA-Z0-9]+", ' ', fileOutput).lower()

	# Generating ngram models
	ng = ngram(cleanFileOutput)

	#unigram

	#bigram

	#trigram
	
main()
