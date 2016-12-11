import facebook
import json

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
	"""
	while "data" in edge and len(edge['data']) > 0:
		cntLikes += len(edge['data'])
		if "paging" in edge and "next" in edge["paging"]:
			url = edge["paging"]["next"]
			id = url.split("graph.facebook.com")[1].split("/likes")[0].split("/")[-1]
			after_val = edge["paging"]["cursors"]["after"]
			edge = fb_conn.get_object(id + "/likes", limit = 50, after = after_val)
		else:
			break
	return cntLikes"""

ACCESS_TOKEN = "EAACEdEose0cBADjzZB83AYB8vf6GNHxLLZAgjO2l5ZAx2Lv4LT1uSY2MPxxRvuqDDZCxY9y6xzQHZBy4ZAmjRcMuSrKUcZC7OKbTgCqWtQfDSO5d62HwlRvQNhbZAJJsbomlD5NqHtWZA20Kdgbo9qyHsBjqVJvjk4ZCYMZB3oD6NjobQZDZD"
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