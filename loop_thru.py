#First read in the data from the text file, soon we will be reading from social media
test_str = open("gmrTweets.txt").read()

test_dic = eval(test_str)

#print test_dic["text"]

'''
for key in test_dic:
	print key
'''

'''
for key in test_dic:
	print key, test_dic[key]
'''

'''
for key in test_dic:
	print key, isinstance(test_dic[key], dict)
'''

'''
for key in test_dic["user"]:
	print "user", key, test_dic["user"][key]
'''

'''
for key in test_dic["entities"]:
	print "entities", key, isinstance(test_dic["entities"][key], list), len(test_dic["entities"][key])
'''

'''
for key in test_dic["entities"]["urls"][0]:
	print "entities urls", key, test_dic["entities"]["urls"][0][key]
'''

print test_dic["entities"]["urls"][0]["display_url"]