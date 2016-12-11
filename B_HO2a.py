from bs4 import BeautifulSoup
import requests
import json
import codecs
import nltk

def removeUnicode(text):
	asciiText = ""
	for char in text:
		if (ord(char) < 128):
			asciiText += char
	return asciiText

nltk.download("stopwords")

QRY = ["swift", "interbank", "rules"]
html = requests.get("http://www.swift.com/insights/press-releases/swift-and-cips-co_sign-memorandum-of-understanding-on-cross-border-interbank-payment-system-cooperation")
soup = BeautifulSoup(html.text, "html5lib")
all_paras = soup.find_all("p")

data_2016 = ""
for para in all_paras:
	data_2016 += para.text

asc_2016 = removeUnicode(data_2016)
lstSent = nltk.tokenize.sent_tokenize(asc_2016)
sentences = [sent.lower().split() for sent in lstSent]
tc = nltk.TextCollection(sentences)

for sentNo in range(len(sentences)):
	tfidf = 0
	for term in [t.lower() for t in QRY]:
		tfidf += tc.tf_idf(term, sentences[sentNo])
	if tfidf > 0:
		print "TF/IDF score %s for this sentence" % tfidf
		print " ".join(sentences[sentNo])
		print