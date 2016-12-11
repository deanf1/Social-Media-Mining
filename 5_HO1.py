import twitter

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
tw = twitter.Twitter(auth = auth)

q = "@twitterapi"
count = 2
tweets = tw.search.tweets(q = q, count = count, lang = "en")
for status in tweets["statuses"]:
	print status["text"].encode("utf-8")
print "======================================================================="

count = 1
tweets = tw.search.tweets(q = q, count = count, lang = "en")
for status in tweets["statuses"]:
	print status["text"].encode("utf-8")
print "======================================================================="

for item in tweets["search_metadata"]:
	print item, tweets["search_metadata"][item]

nextSet = tweets["search_metadata"]["next_results"]

next_maxID = nextSet.split("max_id=")[1].split('&')[0]
print next_maxID
print "======================================================================="

tweets = tw.search.tweets(q = q, count = count, include_entitites = "true", max_id = next_maxID)
print "======================================================================="
for status in tweets["statuses"]:
	print status["text"].encode("utf-8")