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
tw = twitter.Twitter(auth=auth)

q = "@twitterapi"
count = 1
tweets = tw.search.tweets(q = q, count = count, lang = "en")
for item in tweets["statuses"][0]["entities"]:
	print item, tweets["statuses"][0]["entities"][item]
print "======================================================================="

if tweets["statuses"][0]["entities"]["user_mentions"]:
	for field in tweets["statuses"][0]["entities"]["user_mentions"]:
		print field
	print "======================================================================="
	print tweets["statuses"][0]["entities"]["user_mentions"][0]["id_str"]
else:
	print "No User mentions the go around"

print

if tweets["statuses"][0]["entities"]["urls"]:
	tweets["statuses"][0]["entities"]["urls"]
else:
	print "No URLs this go around"

print

if tweets["statuses"][0]["entities"]["hashtags"]:
	for field in tweets["statuses"][0]["entities"]["hashtags"]:
		print field
	print tweets["statuses"][0]["entities"]["hashtags"][0]["text"]
else:
	print "No hashtags this go around"
print "======================================================================="

if tweets["statuses"][0]["user"]:
	print tweets["statuses"][0]["user"].keys()
	print tweets["statuses"][0]["user"]["screen_name"].encode("utf-8")
	print tweets["statuses"][0]["user"]["description"].encode("utf-8")
	print tweets["statuses"][0]["user"]["location"].encode("utf-8")
	print "======================================================================="
else:
	print "No user data this go around"

count = 10
tweets = tw.search.tweets(q = q, count = count, lang = "en")
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "Here are text messages"
for status in tweets["statuses"]:
	print status["text"].encode("utf-8")