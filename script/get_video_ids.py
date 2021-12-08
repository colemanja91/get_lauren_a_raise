#!/usr/bin/python3

import json
from youtube import youtube

client = youtube()

PLAYLIST_ID = "UU6MnY4d56I8j2H327vZzmFg"

def video_ids():
  videos = []

  hasMore = True
  pageToken = None

  while hasMore:
    print("Requesting...")
    videoRequest = client.playlistItems().list(
      part="snippet,contentDetails,status",
      playlistId=PLAYLIST_ID,
      maxResults=50,
      pageToken=pageToken
    ).execute()

    items = videoRequest["items"]
    videos.extend(items)

    print(f"Retrieved {len(items)} items")

    if ('nextPageToken' in videoRequest):
      pageToken = videoRequest["nextPageToken"]
      hasMore = True
    else:
      hasMore = False
  
  print(f"Done! Total retrieved: {len(videos)}")
  return videos

if __name__ == '__main__':
  videos = video_ids()

  print("Writing results")
  with open("./data/videos/list.json", "w") as fopen:
    json.dump(videos, fopen)
