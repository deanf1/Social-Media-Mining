library(aod)
library(ggplot2)
library(Rcpp)

mydata <- read.csv("http://www.ats.ucla.edu/stat/data/binary.csv")

head(mydata)
summary(mydata)
sapply(mydata, sd)