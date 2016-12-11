import twitter
import json
from collections import Counter
from prettytable import PrettyTable

def removeUnicode(text):
	asciiText = ""
	for char in text:
		if(ord(char) < 128):
			asciiText = asciiText + char
	return asciiText

CONSUMER_KEY = "7krew915QHP13UvyVX2eDLpEo"
CONSUMER_SECRET = "807mQbdvx6uJWSnpsyQG46DIdbPok6QlE2ZVP9uohA6Vhkd0tC"
OAUTH_TOKEN = "740666174460067842-yJjkzxTXEanWM7ADUXIyqSbuxXgeNLZ"
OAUTH_TOKEN_SECRET = "D0T32ePXGcf6PROaf0ULQBWsSI3PgIB31oH76gRkbFg9v"
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
tw = twitter.Twitter(auth=auth)

q = "@twitterapi"
count = 10
tweets = tw.search.tweets(q = q, count = count, lang  = "en")
texts = []
for status in tweets["statuses"]:
	texts.append(status["text"])
print texts

print "======================================================================="

words = []
for text in texts:
	for w in text.split():
		words.append(w)
print words

cnt = Counter(words)

pt = PrettyTable(field_names = ["Word", "Count"])
srtCnt = sorted(cnt.items(), key = lambda pair:pair[1], reverse = True)
for kv in srtCnt:
	pt.add_row(kv)
print pt

print "======================================================================="

print "Lexical Diversity"
print 1.0 * len(set(words)) / len(words)