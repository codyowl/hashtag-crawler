

# function to create google docs
def create_google_docs(title):
	
	body = {
	    'title': title
	}
	doc = service.documents() \
	    .create(body=body).execute()
	print('Created document with title: {0}'.format(doc.get('title')))

def inserting_tweets_to_google_docs(tweets):
	requests = [
         {
            'insertText': {
                'location': {
                    'index': 25,
                },
                'text': tweets
            }
        },
    ]

    result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
