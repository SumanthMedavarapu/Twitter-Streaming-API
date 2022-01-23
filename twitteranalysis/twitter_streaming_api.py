import tweepy
import config
import json

client = tweepy.Client(bearer_token=config.bearer_token)
query = 'Justin Bieber -sound -music -singing -rock -tune -melody -is:retweet '
response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'])
users = {u['id']: u for u in response.includes['users']}

# To get more than 100 tweets
tweets_json = {'tweet_details':[]}
for tweet in tweepy.Paginator(client.search_recent_tweets,query = query, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'], max_results = 100).flatten(limit = 1000):
    user = users.get(tweet.author_id)
    tweet_dict = {'id': tweet.id, 'text': tweet.text, 'created_at': str(tweet.created_at)}
    if user:
        tweet_dict['user_profile_url'] = user.profile_image_url

    tweets_json["tweet_details"].append(tweet_dict)

# Data is written into json file
with open("tweets.json", "w") as file_handler:
    json.dump(tweets_json, file_handler)

# getting tweet counts
def count_recent_tweets(query):
    counts = client.get_recent_tweets_count(query = query, granularity = 'day')
    for count in counts.data:
        print(count)


unique_tweets = 'Justin Bieber -sound -music -singing -rock -tune -is:retweet '
all_tweets = 'Justin Bieber -sound -music -singing -rock -tune '
count_recent_tweets(unique_tweets)
count_recent_tweets(all_tweets)
