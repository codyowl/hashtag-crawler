import tweepy
from tweepy import Cursor


class TweepyApi:
	# function to auth with the twitter credentials
	def tweepy_auth(self,consumer_key, consumer_secret, access_token, access_token_secret):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret

		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)
		self.api = tweepy.API(self.auth)
		return self.api

	# function to use Cursor to get all tweets based on hashtags
	def tweepy_cursor(self,id, hashtag):
		self.id = id
		self.hashtag = hashtag

		self.tweets_list = []
		for tweet in tweepy.Cursor(self.api.user_timeline,id=self.id).items():
			if self.hashtag in tweet.text:
				print (tweet.text)
				self.tweets_list.append(tweet.text)
		return self.tweets_list		