import json
import requests
import html5lib
import twitter
from bs4 import BeautifulSoup

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

URL = "https://twitter.com/search?q=%40twitterapi&src=typd"
html = requests.get(URL).text
soup = BeautifulSoup(html, "html5lib")
fp_text = soup.p.text
print fp_text
all_paras = soup.find_all('p')
for para in all_paras:
	print para.text.encode("utf-8")

q = "@twitterapi"
count = 100
for status in tw.search.tweets(q=q, count=count)["statuses"]:
	if status["lang"] == "en":
		print json.dumps(status["text"]).encode("utf-8")