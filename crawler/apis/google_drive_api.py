import pygsheets
import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
credentials_dir_path = '/'.join(ROOT_DIR.split('/')[:-1])
google_credentials_path = credentials_dir_path + '/credentials/credentials.json'

class GoogleDriveApi:
	def __init__(self, service_name, title, tweets_list):
		self.service_name =  service_name
		self.title = title
		self.tweets_list = tweets_list
		if os.path.exists(google_credentials_path):
			self.authorization = pygsheets.authorize(service_file=google_credentials_path)
		else:
			raise FileNotFoundError

	def write_tweets_to_google_sheets(self):
		data_frame = pd.DataFrame()
		data_frame['tweets'] = self.tweets_list
		google_sheets = self.authorization.open(self.title)
		first_sheet = google_sheets[0]
		first_sheet.set_dataframe(df,(1,1))



