import tweepy
import random

# Define your Twitter API keys and secrets
consumer_key = "<YOUR_CONSUMER_KEY>"
consumer_secret = "<YOUR_CONSUMER_SECRET>"
access_token = "<YOUR_ACCESS_TOKEN>"
access_token_secret = "<YOUR_ACCESS_TOKEN_SECRET>"

# Authenticate your Twitter API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a new tweepy API instance
api = tweepy.API(auth)

# Search for tweets containing a random word
word = random.choice(["love", "hate", "happy", "sad"])
tweets = tweepy.Cursor(api.search, word).items(1)

# Write the first tweet to your timeline
tweet = next(tweets)
api.update_status(tweet.text)
