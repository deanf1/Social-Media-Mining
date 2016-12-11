# The line:
# tweets_corpus <- tm_map(tweets_corpus, function(x) iconv(enc2utf8(x$content), sub = "byte"))
# was found here: http://stackoverflow.com/questions/9637278/r-tm-package-invalid-input-in-utf8towcs
# and here: http://stackoverflow.com/questions/27478161/error-in-enc2utf8x-argumemt-is-not-a-character-vector
# I added it because the plots won't work because emojis characters refuse to encode. It only works some of the time with it added.

library(twitteR)
library(tm)
library(wordcloud)
library(plyr)

# Authenticates and connects to Twitter
api_key <- "7krew915QHP13UvyVX2eDLpEo"
api_secret <- "807mQbdvx6uJWSnpsyQG46DIdbPok6QlE2ZVP9uohA6Vhkd0tC"
access_token <- "740666174460067842-yJjkzxTXEanWM7ADUXIyqSbuxXgeNLZ"
access_token_secret <- "D0T32ePXGcf6PROaf0ULQBWsSI3PgIB31oH76gRkbFg9v"
setup_twitter_oauth(api_key, api_secret, access_token, access_token_secret)

# Coca Cola Analysis
tweets <- searchTwitter("@cocacola -filter:retweets", n = 25)

tweets_txt <- ldply(tweets, statusText)
tweets_vect = tweets_txt$V1
tweets_corpus <- Corpus(VectorSource(tweets_vect))
tweets_corpus <- tm_map(tweets_corpus, function(x) iconv(enc2utf8(x$content), sub = "byte"))
tweets_corpus <- tm_map(tweets_corpus, tolower)
tweets_corpus <- tm_map(tweets_corpus, removePunctuation)
tweets_corpus <- tm_map(tweets_corpus, function(x) removeWords(x, stopwords()))
tweets_corpus <- tm_map(tweets_corpus, PlainTextDocument)


par(ask = TRUE)

wordcloud(tweets_corpus)

tweets_tdm <- TermDocumentMatrix(tweets_corpus, control = list(removePunctuation = TRUE, stopwords = TRUE))
findFreqTerms(tweets_tdm, lowfreq = 10)
findAssocs(tweets_tdm, "cloud", .49)
tweets2_tdm <- removeSparseTerms(tweets_tdm, sparse = 0.90)
tweets2_m <- as.matrix(tweets2_tdm)
tweets2_dist <- dist(tweets2_m, method = "euclidean")

plot(hclust(tweets2_dist), main = "Coca Cola Cluster")

# Pepsi Analysis
tweets <- searchTwitter("@pepsi -filter:retweets", n = 25)

tweets_txt <- ldply(tweets, statusText)
tweets_vect = tweets_txt$V1
tweets_corpus <- Corpus(VectorSource(tweets_vect))
tweets_corpus <- tm_map(tweets_corpus, function(x) iconv(enc2utf8(x$content), sub = "byte"))
tweets_corpus <- tm_map(tweets_corpus, tolower)
tweets_corpus <- tm_map(tweets_corpus, removePunctuation)
tweets_corpus <- tm_map(tweets_corpus, function(x) removeWords(x, stopwords()))
tweets_corpus <- tm_map(tweets_corpus, PlainTextDocument)


par(ask = TRUE)

wordcloud(tweets_corpus)

tweets_tdm <- TermDocumentMatrix(tweets_corpus, control = list(removePunctuation = TRUE, stopwords = TRUE))
findFreqTerms(tweets_tdm, lowfreq = 10)
findAssocs(tweets_tdm, "cloud", .49)
tweets2_tdm <- removeSparseTerms(tweets_tdm, sparse = 0.90)
tweets2_m <- as.matrix(tweets2_tdm)
tweets2_dist <- dist(tweets2_m, method = "euclidean")

plot(hclust(tweets2_dist), main = "Pepsi Cluster")