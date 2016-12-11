import twitter

US_WOEID = 23424977

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

lstTrends = tw.trends.place(_id=US_WOEID)
for trend in lstTrends[0]["trends"]:
	print trend["name"].encode("utf-8")
	