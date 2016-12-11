from pymongo import MongoClient
import twitter
import json

CONSUMER_KEY = "7krew915QHP13UvyVX2eDLpEo"
CONSUMER_SECRET = "807mQbdvx6uJWSnpsyQG46DIdbPok6QlE2ZVP9uohA6Vhkd0tC"
OAUTH_TOKEN = "740666174460067842-yJjkzxTXEanWM7ADUXIyqSbuxXgeNLZ"
OAUTH_TOKEN_SECRET = "D0T32ePXGcf6PROaf0ULQBWsSI3PgIB31oH76gRkbFg9v"
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
tw = twitter.Twitter(auth = auth)

q = "Homer Laughlin"

conn = MongoClient("localhost", 27017)
db = conn.gmrDB
hlc = db.cmsc491

LIMIT = 10
count = 100

for i in range(0, LIMIT):
	if (i == 0):
		tweets = tw.search.tweets(q = q, count = count, lang = "en")
	else:
		tweets = tw.search.tweets(q = q, count = count, include_entities = "true", max_id = nextID)

	for res in tweets["statuses"]:
		try:
			hlc.insert(res)
		except:
			print "insert issue, usually dup"

	try:
		newBlock = tweets["search_metadata"]["next_results"]
		nextID = newBlock.split("max_id=")[1].split("&")[0]
	except:
		print "hit end of hlc tweets"
		break