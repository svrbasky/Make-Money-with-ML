import tweepy
from textblob import textblob

# Obtain these 4 variables by authenticating from Twitter API
consumer_key =
consumer_secret =

access_token = 
access_token_secret = 


# Authentication
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# Search for Tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

