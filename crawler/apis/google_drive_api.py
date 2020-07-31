
class GoogleDriveApi:
    # function to create google docs
    def create_google_docs(self,title):
        self.title = title
    	
    	body = {
    	    'title': self.title
    	}
    	doc = service.documents() \
    	    .create(body=body).execute()
    	print('Created document with title: {0}'.format(doc.get('title')))

    def inserting_tweets_to_google_docs(self, tweets):
        self.tweets = tweets

    	requests = [
             {
                'insertText': {
                    'location': {
                        'index': 25,
                    },
                    'text': self.tweets
                }
            },
        ]

        result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
