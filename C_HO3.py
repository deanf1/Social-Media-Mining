import facebook
import json
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

def removeUnicode(text):
	asciiText = ""
	for char in text:
		if (ord(char) < 128):
			asciiText += char
	return asciiText

def count_likes(id, fb_conn):
	cntLikes = 0
	edge = fb_conn.get_object("/" + id + "/likes", limit = 1, summary = "true")
	return edge["summary"]["total_count"]

ACCESS_TOKEN = "EAACEdEose0cBAO3ZCGlHNimxQyKGD5Pk0SZCnB2fSf6K2YKFYkdIYqvHy9hdFixE1IPOO6cU937S18ZCyDCrlhJSIuZCvE6tOYZBuBDDPw53zS7Ba6im5m9loL4ERYtUILDosfZANWxVHZBBCz0kQM5IGKXEmVZCjwZBpEue9eFZBVsAZDZD"
fb = facebook.GraphAPI(ACCESS_TOKEN)
d_id = fb.request("search", {"q":"Greta Garbo", "type":"page", "limit":5})
print d_id

greta = "17287115271"
d_posts = fb.get_connections(greta, connection_name = "posts")
print "Greta posts ", len(d_posts)
print "Length of D posts is ", len(d_posts["data"])

with open("gPost.txt", "w") as f:
	f.write(str(d_posts))
	f.close()

for post in d_posts["data"]:
	print post["message"].encode("utf-8")
	if "id" in post:
		print "has id number ", post["id"], 
		print " and like count ", count_likes(post["id"], fb)
	else:
		with open ("no_obj.txt", "a") as o:
			o.write(str(d_posts))
			o.close()
	print "---"

print "\nThe first comment on the second post is\n", d_posts["data"][1]["comments"]["data"][0]

pepsi_id = "PepsiUS"
coke_id = "CocaCola"
hillary = "889307941125736"
donald = "153080620724"
print "Greta likes:\t%d" % fb.get_object(greta)["likes"]
print "Coke likes:\t%d" % fb.get_object(coke_id)["likes"]
print "Pepsi likes:\t%d" % fb.get_object(pepsi_id)["likes"]
print "Hillary likes:\t%d" % fb.get_object(hillary)["likes"]
print "Donald likes:\t%d" % fb.get_object(donald)["likes"]

vs_tot = 0
vs_pos = 0
vs_neg = 0
num_cmt = 0
for dataItem in d_posts["data"][1]["comments"]["data"]:
	print removeUnicode(dataItem["message"])
	for datas in dataItem:
		if datas == "from":
			gmrFrom = ""
			for cmtName in dataItem["from"]:
				gmrFrom += dataItem["from"][cmtName].encode("utf-8") + ":"
			gmrFrom = "---- From: " + gmrFrom
		if datas == "like_count":
			likes = "---- Like Count: " + str(dataItem["like_count"])
	print gmrFrom
	print likes

	vs = vaderSentiment(dataItem["message"].encode("utf-8"))
	print "---- Sentiment: " + str(vs["compound"])
	vs_tot += vs["compound"]
	num_cmt += 1
	if vs["compound"] < 0:
		vs_neg += 1
	else:
		vs_pos += 1