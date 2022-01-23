from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
tweets_db = client["tweetsdb"]
tweets_collection = tweets_db["storetweets"]

f = open('tweets.json')
data = json.load(f)
# Iterating through the json
# list
for record in data['tweet_details']:
    tweets_collection.insert_one(record)

print("Insertion Completed")

# Closing file
f.close()

# prints all the records
for record in tweets_collection.find({}):
    print(record)




