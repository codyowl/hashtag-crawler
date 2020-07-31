import tweepy
from tweepy import Cursor

# function to auth with the twitter credentials
def tweepy_auth(consumer_key, consumer_secret, access_token, access_token_secret):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api

# function to use Cursor to get all tweets based on hashtags
def tweepy_cursor(api, id, hashtag):
	tweets_list = []
	for tweet in tweepy.Cursor(api.user_timeline,id=id).items():
		if hashtag in tweet.text:
			print (tweet.text)
			tweets_list.append(tweet.text)
	return tweets_list		