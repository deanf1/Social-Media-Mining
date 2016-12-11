import datetime
import time
import string
from twython import TwythonStreamer
from collections import Counter
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if data["lang"] == "en":
			tweets.append(data)
		if len(tweets) >= 100:
			self.disconnect()
	def on_error(self, status_code, data):
		print status_code, data
		self.disconnect()

CONSUMER_KEY = "7krew915QHP13UvyVX2eDLpEo"
CONSUMER_SECRET = "807mQbdvx6uJWSnpsyQG46DIdbPok6QlE2ZVP9uohA6Vhkd0tC"
OAUTH_TOKEN = "740666174460067842-yJjkzxTXEanWM7ADUXIyqSbuxXgeNLZ"
OAUTH_TOKEN_SECRET = "D0T32ePXGcf6PROaf0ULQBWsSI3PgIB31oH76gRkbFg9v"
stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

gmrCnt = 1
while (gmrCnt == 1):
	tweets = []
	gmrStart = str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
	stream.statuses.filter(track = "data")
	gmrEnd = str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
	with open("umbc.txt", "a") as myfile:
		for gmrText in tweets:
			if (gmrText["user"]["description"] is not None) and (gmrText["user"]["location"] is not None):
				myfile.write(str(gmrText["id"]))
				myfile.write(", ")
				rplText = string.replace(gmrText["text"].encode("utf-8"), "\r", "<cr>")
				myfile.write(string.replace(rplText, "\n", "<nl>"))
				myfile.write(", ")
				rplDesc = string.replace(gmrText["user"]["description"].encode("utf-8"), "\r", "<cr>")
				myfile.write(string.replace(rplDesc, "\n", "<nl>"))
				myfile.write(", ")
				myfile.write(gmrText["user"]["location"].encode("utf-8"))
				myfile.write(", ")
				myfile.write(gmrStart)
				myfile.write(", ")
				myfile.write(gmrEnd)
				myfile.write("\n")
				print gmrText["text"].encode("utf-8")
				vs = vaderSentiment(gmrText["text"].encode("utf-8"))
				print "\n\t" + str(vs["compound"])
	gmrCnt = 2
	time.sleep(30)