import requests
import json
import codecs
import nltk
import russell as ru
from bs4 import BeautifulSoup

def removeUnicode(text):
	asciiText = ""
	for char in text:
		if(ord(char) < 128):
			asciiText = asciiText + char
	return asciiText

fileObj = codecs.open("Clearing.rtf", "w", "UTF")
html = requests.get("http://www.reuters.com/article/us-china-yuan-payments-exclusive-idUSKBN0M50BV20150309")

soup = BeautifulSoup(html.text, "html5lib")
all_paras = soup.find_all("p")

data_2016 = ""
for para in all_paras:
	fileObj.write(para.text)
	data_2016 = data_2016 + para.text
asc_2016 = removeUnicode(data_2016)

lstSent = nltk.tokenize.sent_tokenize(asc_2016)
print type(lstSent), "sent type"

words = []
for sentence in lstSent:
	for word in nltk.tokenize.word_tokenize(sentence):
		words.append(word.lower())

frqDist = nltk.FreqDist(words)
print "dfrq", type(frqDist)

word_cnt = 0
for item in frqDist.items():
	word_cnt = word_cnt + item[1]
unique_word_cnt = len(frqDist.keys())

hapaxNo = len(frqDist.hapaxes())

skips = [	"and", ".", "to", ",", "the", "for", "in", "of", "that", "a", "on",
			"is", "get", "you", "has", "as", "at", "are", "'", "an", "with",
			"will", "not", "have", "would", "so", "", "but", ":", "be", "like",
			"if", "should", "also", "there", "or", "by", "per"]

mostFreq = []
for w in frqDist.items():
	if w[0] not in skips:
		mostFreq.append(w)

print "Clearing House Article"
print "Num lstSent: ".ljust(25), len(lstSent)
print "Num words: ".ljust(25), word_cnt
print "Num unique words: ".ljust(25), unique_word_cnt
print "Num Hapaxes: ".ljust(25), hapaxNo
print "The most frequent words follow"
mostFreq.sort(key = lambda c : c[1])
for w in mostFreq[-10:]:
	print w[0].encode("utf-8"), "\thas a count of ", w[1]

sentWords = [nltk.tokenize.word_tokenize(s) for s in lstSent]
posWords = [nltk.pos_tag(w) for w in sentWords]
posWords = [token for sent in posWords for token in sent]

for (token, pos) in posWords:
	print token, pos

chunkCollector = []
foundChunk = []
lastPos = None
for (token, pos) in posWords:
	if pos == lastPos and pos.startswith("NN"):
		foundChunk.append(token)
	elif pos.startswith("NN"):
		if foundChunk != []:
			#here, something in hopper so add to collection
			chunkCollector.append(("".join(foundChunk), pos))
		foundChunk = [token]
	lastPos = pos

dChunk = {}
for chunk in chunkCollector:
	dChunk[chunk] = dChunk.get(chunk, 0) + 1

print "For Clearing House Article"
for (entity, pos) in dChunk:
	if entity.istitle():
		print "\t%s (%s)" % (entity, dChunk[entity, pos])

CIPS_sum = ru.summarize(data_2016)
print "Summary of CIPS Article"
print "Print Three Sentence Summary"
for sent in CIPS_sum['top_n_summary']:
	print removeUnicode(sent)