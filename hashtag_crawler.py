from clint.textui import colored, puts
import yaml
from tweepy_api import tweepy_auth

# function for ascii menu
def tool_menu():
	ascii_menu_drawing = r"""
       ,_    /) (\    _,
        >>  <<,_,>>  <<
       //   _0.-.0_   \\
       \'._/       \_.'/
        '-.\.--.--./.-'
        __/ : :Y: : \ _
';,  .-(_| : : | : : |_)-.  ,:'
  \\/.'  |: : :|: : :|  `.\//
   (/    |: : :|: : :|    \)
         |: : :|: : :;
        /\ : : | : : /\
       (_/'.: :.: :.'\_)
        \\  `""`""`  //
         \\         //
          ':.     .:'

    A CLI TOOL FOR CRAWLING TWEETS


	"""

	puts(colored.yellow(ascii_menu_drawing))

# function to read the credentials from yaml file
def read_credentials_yml_file():
	with open("twitter_credentials.yaml") as file:
		credentials_dict = yaml.load(file, Loader=yaml.FullLoader)
	return credentials_dict
	


if __name__ == "__main__":
	tool_menu()
	credentials_dict = read_credentials_yml_file()
	# reading credentials from yaml file
	consumer_key = credentials_dict[CONSUMER_KEY]
	consumer_secret = credentials_dict[CONSUMER_SECRET]
	access_token = credentials_dict[ACCESS_TOKEN]
	access_token_secret = credentials_dict[ACCESS_TOKEN_SECRET]

	# authenticating using tweepy
	api = tweepy_auth(consumer_key, consumer_secret, access_token, access_token_secret)
