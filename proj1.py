"""
Dean Fleming <deanf1@umbc.edu>

CMSC491 - Project 1

I used the Search API because I figured that Coca Cola and Pepsi aren't exactly 
controversial topics, so a history of the past week's tweets might be more
substantial than what the next few people say.

Note: I excluded retweets from my queries because the Coca Cola and Pepsi
Twitter pages are so popular that my results were almost entirely retweets of 
one post that either Coca Cola or Pepsi made. I wanted to see what Twitter users
are really saying about them.
"""

import twitter
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

# Removes Unicode characters (emojis, etc.)
def removeUnicode(text):
	asciiText = ""
	for char in text:
		if(ord(char) < 128):
			asciiText = asciiText + char
	return asciiText

# Prints out the given amount of tweets for the given query, along with each
# message's lexical analysis and sentiment analysis
def printAndGetTweetInfo(query, count):
	totalDiversity = 0.0
	totalSentiment = 0.0

	tweets = tw.search.tweets(q = query, count = count, lang = "en")

	for status in tweets["statuses"]:
		print removeUnicode(status["text"].encode("utf-8"))
		print 
		print "Favorites: ", status["favorite_count"], ", Retweets: ", status["retweet_count"]
		totalDiversity += printLexicalAnalysis(status)
		totalSentiment += printSentimentAnalysis(status)
		print "======================================================================="

	totalDiversity /= count
	totalSentiment /= count 
	return tweets, totalDiversity, totalSentiment

# Finds, prints out, and returns the lexical analysis
def printLexicalAnalysis(status):
	words = []
	for word in (status["text"].encode("utf-8")).split():
			words.append(word)
	diversity = 1.0 * len(set(words)) / len(words)
	print "Lexical Diversity: ", diversity
	return diversity

# Finds, prints out, and returns the sentiment analysis
def printSentimentAnalysis(status):
	vader = vaderSentiment(status["text"].encode("utf-8"))
	sentiment = str(vader["compound"])
	print "Sentiment: ", sentiment
	return vader["compound"]

# Authenticates and connects to Twitter 
CONSUMER_KEY = "7krew915QHP13UvyVX2eDLpEo"
CONSUMER_SECRET = "807mQbdvx6uJWSnpsyQG46DIdbPok6QlE2ZVP9uohA6Vhkd0tC"
OAUTH_TOKEN = "740666174460067842-yJjkzxTXEanWM7ADUXIyqSbuxXgeNLZ"
OAUTH_TOKEN_SECRET = "D0T32ePXGcf6PROaf0ULQBWsSI3PgIB31oH76gRkbFg9v"
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
tw = twitter.Twitter(auth = auth)

# Searches for and prints out 25 tweets for Coca Cola and Pepsi
print
print "======================================================================="
print "============================== Coca Cola =============================="
print "======================================================================="
cokeTweets, cokeDiversity, cokeSentiment = printAndGetTweetInfo("@cocacola -filter:retweets", 25)

print
print
print
print "======================================================================="
print "================================ Pepsi ================================"
print "======================================================================="
pepsiTweets, pepsiDiversity, pepsiSentiment = printAndGetTweetInfo("@pepsi -filter:retweets", 25)

# Prints a summary of the lexiacl and sentiment analyses
print
print
print
print "======================================================================="
print "=============================== Summary ==============================="
print "======================================================================="
print "Overall Coca Cola Lexical Diversity:\t", cokeDiversity
print "Overall Pepsi Lexical Diversity:\t", pepsiDiversity
print "Overall Coca Cola Sentiment:\t\t", cokeSentiment
print "Overall Pepsi Sentiment:\t\t", pepsiSentiment