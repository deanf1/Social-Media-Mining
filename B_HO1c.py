from pymongo import MongoClient
import json

conn = MongoClient("localhost", 27017)
db = conn.gmrDB
hlc = db.cmsc491

rs = hlc.find()
print rs[0]

for res in rs:
	print res["id"], res["text"].encode("utf-8")