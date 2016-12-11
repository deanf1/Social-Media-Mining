import requests
import json
ACCESS_TOKEN = "EAACEdEose0cBADjzZB83AYB8vf6GNHxLLZAgjO2l5ZAx2Lv4LT1uSY2MPxxRvuqDDZCxY9y6xzQHZBy4ZAmjRcMuSrKUcZC7OKbTgCqWtQfDSO5d62HwlRvQNhbZAJJsbomlD5NqHtWZA20Kdgbo9qyHsBjqVJvjk4ZCYMZB3oD6NjobQZDZD"
fb_url = "https://graph.facebook.com/me"
fields = "id,name"
url = "%s?fields=%s&access_token=%s" % (fb_url, fields, ACCESS_TOKEN)
results = requests.get(url).json()
print json.dumps(results, indent = 1)