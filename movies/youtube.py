from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyAj9-ZI6zpKGMqnta5bAmmHo6oGDG5pad8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	# Call the search.list method to retrieve results matching the specified
	# query term.
	search_response = youtube.search().list(
	q=options['q'],
	part="id,snippet",
	maxResults=options['max_results']
	).execute()


	# Add each result to the appropriate list, and then display the lists of
	# matching videos, channels, and playlists.
	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			movie_url = 'https://www.youtube.com/watch?v=' + search_result['id']['videoId']
			return movie_url
		else:
			return ''


def execute_youtube_search(args):
	try:
		return youtube_search(args)
	except HttpError:
		print("An HTTP error occurred")
		return ''
