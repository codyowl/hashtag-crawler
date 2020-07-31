import requests
import json

GITHUB_URL = 'https://api.github.com/gists'

class GitHubApi:
	# function to authenticate
	def authenticate_github_api(self,github_access_token, github_user_name):
		self.github_access_token = github_access_token
		self.github_user_name = github_user_name
		self.git_auth_response = requests.get(
			GITHUB_URL, 
			auth=(self.github_user_name, self.github_access_token)
			)
		
	# function to create git gist
	def create_git_gist(self,gist_title, tweets_list):
		self.gist_title = gist_title
		self.tweets_list = tweets_list
		
		headers = {'Authorization':'token %s' % (self.github_access_token)}
		params = {'scope':'gist'}
		payload = {"description":"GIST created by hashtag crawler",
				 "public":True,
			}
		payload['files'] = {}
		payload['files'][self.gist_title] = {} 
		# converting the data from tweets list to string
		tweets = ""
		for tweet in self.tweets_list:
			tweets += str(tweet)
		payload['files'][self.gist_title]['content'] = tweets   

		try:
			response = requests.post(GITHUB_URL,headers=headers,params=params,data=json.dumps(payload))
		except Exception as e:
			print (e)

		print ("git gist created")

