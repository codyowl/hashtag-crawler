from clint.textui import colored, puts
import yaml
from tweepy_api import tweepy_auth, tweepy_cursor
from git_api import create_git_gist
import tweepy
import time

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

                                        A SIMPLE CLI TOOL FOR CRAWLING TWEETS

                USAGE : crawl --id <twitter_id> --hashtag <hashtag> --save <git,docs,evernote>                                     
"""       

# function for ascii menu
def tool_menu():
    puts(colored.yellow(ascii_menu_drawing))

# function to read the credentials from yaml file
def read_credentials_yml_file():
    with open("access_credentials.yaml") as file:
        credentials_dict = yaml.load(file, Loader=yaml.FullLoader)
    return credentials_dict

# function to give credential got from yaml file 
def get_credentials(credentials_dict, twitter=None, github=None, evernote=None):
    if twitter:
        twitter_consumer_key = credentials_dict['TWITTER_CONSUMER_KEY']
        twitter_consumer_secret = credentials_dict['TWITTER_CONSUMER_SECRET']
        twitter_access_token = credentials_dict['TWITTER_ACCESS_TOKEN']
        twitter_access_token_secret = credentials_dict['TWITTER_ACCESS_TOKEN_SECRET']

        return twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret 
    
    elif github:
        github_access_token = credentials_dict['GIT_HUB_ACCESS_TOKEN']
        github_client_id = credentials_dict['GIT_HUB_CLIENT_ID']
        github_client_secret = credentials_dict['GIT_HUB_CLIENT_SECRET']

        return github_access_token,github_client_id, github_client_secret

    
# function to read all tweets from a particular account based on hashtag
def crawl_tweet_from_account_based_on_hastag(api, id, hashtag):
    tweets_list = tweepy_cursor(api, id, hashtag)
    return tweets_list


if __name__ == "__main__":
    tool_menu()
    # reading credentials from the yaml file
    credentials_dict = read_credentials_yml_file()
    # reading credentials from yaml file for twitter
    twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret = get_credentials(credentials_dict, twitter=True)  
    # reading credentials from yaml file for github
    github_access_token, github_client_id, github_client_secret = get_credentials(credentials_dict, github=True)
    # authenticating using tweepy
    api = tweepy_auth(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret)
    # hardcoding id and hashtag 
    id = "codyowl_"
    hashtag = "#100daysofcode"
    
    tweets_list = crawl_tweet_from_account_based_on_hastag(api, id, hashtag)
    # writing tweets to git gist
    create_git_gist(tweets_list, github_access_token)

