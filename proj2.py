"""
Dean Fleming <deanf1@umbc.edu>

CMSC491 - Project 2

I referenced the following URL for how to do bigrams (since we didn't go over 
it in lecture):
http://stackoverflow.com/questions/21165702/nltk-collocations-for-specific-words
"""

import requests
import json
import codecs
import nltk
import russell as ru
from bs4 import BeautifulSoup
from nltk.collocations import *

# removes Unicode characters
def removeUnicode(text):
	asciiText = ""
	for char in text:
		if(ord(char) < 128):
			asciiText = asciiText + char
	return asciiText

# connects to the website and creates a navigable parse tree
html = requests.get("http://www.ecommercetimes.com/story/52616.html")
soup = BeautifulSoup(html.text, "html5lib")
allParas = soup.find_all("p")

# extracts the text from the paragraphs
textData = ""
for para in allParas:
	textData += para.text

# creates a three sentence summary using the Luhn algorithm
CIPS_sum = ru.summarize(textData)
print 
print "========================================================================"
print "                        Three Sentence Summary:"
print "========================================================================"
for sent in CIPS_sum['top_n_summary']:
	print removeUnicode(sent)

# makes a list of sentences from the paragraph text
lstSent = nltk.tokenize.sent_tokenize(removeUnicode(textData))

# makes a list of words from the sentence list
words = []
for sentence in lstSent:
	for word in nltk.tokenize.word_tokenize(sentence):
		words.append(word.lower())

# finds bigrams
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(words)

# prints the 10 bigrams with the highest PMI
print 
print "========================================================================"
print "                      The Top 10 Strongest Bigrams:"
print "========================================================================"
print finder.nbest(bigram_measures.likelihood_ratio, 10)

# does a frequency distribution on the words
frqDist = nltk.FreqDist(words)

# counts the words
word_cnt = 0
for item in frqDist.items():
	word_cnt += item[1]
unique_word_cnt = len(frqDist.keys())

# list of stop words to skip over
skips = [	"and", ".", "to", ",", "the", "for", "in", "of", "that", "a", "on",
			"is", "get", "you", "has", "as", "at", "are", "'", "an", "with",
			"will", "not", "have", "would", "so", "", "but", ":", "be", "like",
			"if", "should", "also", "there", "or", "by", "per", "'s", "their", 
			"it", "''", "``", "says"]

# finds the most frequent words
mostFreq = []
for w in frqDist.items():
	if w[0] not in skips:
		mostFreq.append(w)

# prints the 10 most frequent words
print
print "========================================================================"
print "                     The Top 10 Most Frequent Words:"
print "========================================================================"
mostFreq.sort(key = lambda c : c[1])
for w in mostFreq[-10:]:
	if len(w[0].encode("utf-8")) <= 7:
		print w[0].encode("utf-8") + "\t\thas a count of " + str(w[1])
	else:
		print w[0].encode("utf-8") + "\thas a count of " + str(w[1])

# find parts of speech
sentWords = [nltk.tokenize.word_tokenize(s) for s in lstSent]
posWords = [nltk.pos_tag(w) for w in sentWords]
posWords = [token for sent in posWords for token in sent]

# print parts of speech
print
print "========================================================================"
print "                            Parts of Speech:"
print "========================================================================"
for (token, pos) in posWords:
	print token, pos

# chunking algorithm
chunkCollector = []
foundChunk = []
lastPos = None
for (token, pos) in posWords:
	if pos == lastPos and pos.startswith("NN"):
		foundChunk.append(token)
	elif pos.startswith("NN"):
		if foundChunk != []:
			chunkCollector.append(("".join(foundChunk), pos))
		foundChunk = [token]
	lastPos = pos

# extract entities
dChunk = {}
for chunk in chunkCollector:
	dChunk[chunk] = dChunk.get(chunk, 0) + 1

# prints entities
print
print "========================================================================"
print "                       Entities from Chunking:"
print "========================================================================"
for (entity, pos) in dChunk:
	if entity.istitle():
		print "\t%s (%s)" % (entity, dChunk[entity, pos])