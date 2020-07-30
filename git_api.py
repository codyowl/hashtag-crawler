import requests
import json

GITHUB_URL = 'https://api.github.com/gists'

# function to authenticate
def authenticate_github_api(github_access_token, github_user_name):
	git_auth_response = requests.get(
		GITHUB_URL, 
		auth=(github_user_name, github_access_token)
		)
	return git_auth_response

# function to create git gist
def create_git_gist(gist_title, tweets_list, git_hub_access_token):
	headers = {'Authorization':'token %s' % (git_hub_access_token)}
	params = {'scope':'gist'}
	payload = {"description":"GIST created by hashtag crawler",
			 "public":True,
		}
	payload['files'] = {}
	payload['files'][gist_title] = {} 
	# converting the data from tweets list to string
	tweets = ""
	for tweet in tweets_list:
		tweets += str(tweet)
	payload['files'][gist_title]['content'] = tweets   

	try:
		response = requests.post(GITHUB_URL,headers=headers,params=params,data=json.dumps(payload))
	except Exception as e:
		print (e)

	print ("git gist created")
