
from google_apis import create_service
from search import videoId
import search
import time
CLIENT_FILE = 'client-secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
]

service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)


video_id = search.videoId

# Example 1. Post A Comment
request_body = {
	'snippet': {
		'videoId': video_id,
		'topLevelComment': {
			'snippet': {
				'textOriginal': 'Hellossags There.'
			}
		}
	}
}

response = service.commentThreads().insert(
	part='snippet',
	body=request_body
).execute()

#rint(response)

