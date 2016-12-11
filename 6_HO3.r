library(twitteR)
library(tm)
library(wordcloud)
library(plyr)

api_key <- "7krew915QHP13UvyVX2eDLpEo"
api_secret <- "807mQbdvx6uJWSnpsyQG46DIdbPok6QlE2ZVP9uohA6Vhkd0tC"
access_token <- "740666174460067842-yJjkzxTXEanWM7ADUXIyqSbuxXgeNLZ"
access_token_secret <- "D0T32ePXGcf6PROaf0ULQBWsSI3PgIB31oH76gRkbFg9v"
setup_twitter_oauth(api_key, api_secret, access_token, access_token_secret)

tweets <- searchTwitter("#umbc", n = 150)

tweets_txt <- ldply(tweets, statusText)
tweets_vect = tweets_txt$V1
tweets_corpus <- Corpus(VectorSource(tweets_vect))
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

plot(hclust(tweets2_dist), main = "Big Data Cluster")