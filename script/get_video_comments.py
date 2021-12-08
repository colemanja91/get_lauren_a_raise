#!/usr/bin/python3

import json
from youtube import youtube

client = youtube()

def load_videos():
  with open("./data/videos/list.json", "r") as fopen:
    videos = json.load(fopen)
  
  return videos

def get_comments_for_video(video_id):
  comments = []

  hasMore = True
  pageToken = None

  while hasMore:
    print("Requesting...")
    commentRequest = client.commentThreads().list(
      part="id,snippet,replies",
      videoId=video_id,
      pageToken=pageToken
    ).execute()

    items = commentRequest["items"]
    comments.extend(items)

    print(f"Retrieved {len(items)} items")

    if ('nextPageToken' in commentRequest):
      pageToken = commentRequest["nextPageToken"]
      hasMore = True
    else:
      hasMore = False
    
  print(f"Done! Total retrieved: {len(comments)}")
  return comments

def get_comments_for_all_videos(videos):
  comments = []

  for video in videos:
    video_id = video["contentDetails"]["videoId"]
    print(f"Getting for video {video_id}")
    video_comments = get_comments_for_video(video_id)
    comments.extend(video_comments)
  
  print("Done!")

  return comments


if __name__ == '__main__':
  videos = load_videos()
  comments = get_comments_for_all_videos(videos)

  with open("./data/comments/raw/comment_threads.json", "w") as fopen:
    json.dump(comments, fopen)
