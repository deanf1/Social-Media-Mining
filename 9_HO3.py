import requests
import json
import codecs
import nltk
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