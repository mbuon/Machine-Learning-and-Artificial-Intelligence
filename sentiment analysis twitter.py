import tweepy
from textblob import TextBlob

#Create your app from apps.twitter.com and fill your keys and tokens
consumer_key = 'XXXX'
consumer_secret = 'XXXXX'
access_token = 'XXXX'
access_token_secret = 'XXXXX'

#Authenticate your application
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Search for tweets
public_tweets = api.search('Tim Cook')
for tweet in public_tweets:
    #Print tweets
    print(tweet.text)
    #Use textblob to fetch sentiment of the tweet
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')