"""This is a sample file for hw2. 
It contains the function that should be submitted,
except all it does is output a random value.
- Dr. Licato"""

from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.naive_bayes
import random
import re

"""
trainFile: a text file, where each line is arbitratry human-generated text
Outputs n-grams (n=2, or n=3, your choice). Must run in under 120 seconds
"""
def calcNGrams_train(trainFile):
	with open(trainFile, 'r', encoding='utf-8') as f:
		paragraphs = f.read()
	f.close()
    
	finalSentences = []
	sentences = re.split("[.!?\n\"]", paragraphs)
	while(" " in sentences):
		sentences.remove(" ")
	for sentence in sentences:
		newSentence = list(filter(None, re.split("^ ", sentence)))
		if newSentence:
			#print(newSentence)
			finalSentences.append(newSentence[0])
	print(finalSentences)

	bigrams = [i for j in finalSentences 
		for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]
    
	# print(bigrams)

	pass #don't return anything from this function!

"""
sentences: A list of single sentences. All but one of these consists of entirely random words.
Return an integer i, which is the (zero-indexed) index of the sentence in sentences which is non-random.
"""
def calcNGrams_test(sentences):
	"""
	make bigrams out of the test sentences
	check bigrams for sentence 1 and give a minus 1 if bigram does not appear
	check 2
	check 3
	return index of lowest score
	"""
	testSentences = sentences
	finalSentences = []
	for sentence in testSentences:
		for letter in sentence:
			sentence.remove(",")
		finalSentences.append(noPuncSentences)
	
	bigrams = [i for j in testSentences 
		for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]
	print(bigrams)
	return random.randint(0, len(sentences)-1)

"""
trainFile: A jsonlist file, where each line is a json object. Each object contains:
	"review": A string which is the review of a movie
	"sentiment": A Boolean value, True if it was a positive review, False if it was a negative review.
"""
def calcSentiment_train(trainFile):
	pass #don't return anything from this function!

"""
review: A string which is a review of a movie
Return a boolean which is the predicted sentiment of the review.
Must run in under 120 seconds, and must use Naive Bayes
"""
def calcSentiment_test(review):
	return random.choice([True, False])

# calcNGrams_train("problem1_trainingFile.txt")

calcNGrams_test(["We have heard her clear, bird-like voice mingling with the scarlet symbol, and the most agreeable of his.", 
	"poetry unthrifty ignominy devoting passages ceases strewn wished concerned progenitors arrangement borne sergeants express contains flowers medicine vain mahogany social",
	"I have ever cherished, and would be convulsed with rage of grief and sob out her love for her."])