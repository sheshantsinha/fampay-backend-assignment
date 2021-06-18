import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(api_key, keyword, max_result=10, page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=api_key)
    try:
        search_response = youtube.search().list(
            q=keyword,
            part='id,snippet',
            pageToken=page_token,
            maxResults=50
        ).execute()
    except Exception as e:
        print("exception", e)
        return [], None, True

    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            search_result['snippet']['video_id'] = search_result['id']['videoId']
            formatted_date = datetime.datetime.strptime(search_result['snippet']["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
            row = (
                search_result['snippet']['video_id'],
                formatted_date.strftime("%Y-%m-%d %H:%M:%S"),
                search_result['snippet']["title"],
                search_result['snippet']["description"],
                search_result['snippet']["thumbnails"]["default"]["url"]
            )
            videos.append(row)
    return videos, search_response["nextPageToken"] if "nextPageToken" in search_response else None, False