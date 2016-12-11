import twitter
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
twitter_api = twitter.Twitter(auth=auth)

q = "data science"
count = 100
search_results = twitter_api.search.tweets(q = q, count = count)
statuses = search_results["statuses"]

retweets = []
for status in statuses:
	if "retweeted_status" in status:
		retweets.append((status["user"]["screen_name"].encode("utf-8"), status["retweet_count"], 
			status["retweeted_status"]["user"]["screen_name"].encode("utf-8"), status["text"].encode("utf-8")))
		g = open("gmrTweet.txt", "w")
		g.write(str(status))
		g.close()
	"""print status["user"]["screen_name"], status["text"].encode("utf-8")
	print"""

pt = PrettyTable(field_names=["Usr", "Count", "rtUsr", "Text"])
[pt.add_row(row) for row in sorted(retweets, key = lambda x : x[1], reverse = True)[:5]]
pt.max_width["Text"] = 40
pt.align = "l"
print pt
