#!/usr/bin/python3

from csv import DictWriter
import json

def load_comment_thread_data():
  with open("./data/comments/raw/comment_threads.json", "r") as fopen:
    data = json.load(fopen)
  
  return data

def extract_comment(data):
  return {
    "commentId": data.get("id", ""),
    "authorDisplayName": data.get("snippet", "").get("authorDisplayName", ""),
    "authorProfileImageUrl": data.get("snippet", "").get("authorProfileImageUrl", ""),
    "authorChannelUrl": data.get("snippet", "").get("authorChannelUrl", ""),
    "channelId": data.get("snippet", "").get("channelId", ""),
    "videoId": data.get("snippet", "").get("videoId", ""),
    "textDisplay": data.get("snippet", "").get("textDisplay", ""),
    "textOriginal": data.get("snippet", "").get("textOriginal", ""),
    "parentId": data.get("snippet", "").get("parentId", ""),
    "canRate": data.get("snippet", "").get("canRate", ""),
    "viewerRating": data.get("snippet", "").get("viewerRating", ""),
    "likeCount": data.get("snippet", "").get("likeCount", ""),
    "moderationStatus": data.get("snippet", "").get("moderationStatus", ""),
    "publishedAt": data.get("snippet", "").get("publishedAt", ""),
    "updatedAt": data.get("snippet", "").get("updatedAt", "")
  }

def extract_comments_from_thread(data):
  comments = []

  comments.append(extract_comment(data["snippet"]["topLevelComment"]))

  for reply in data.get("replies", {}).get("comments", []):
    comments.append(extract_comment(reply))
  
  return comments

def extract_all_comments(data):
  comments = []

  for thread in data:
    comments.extend(extract_comments_from_thread(thread))
  
  return comments

if __name__ == '__main__':
  comment_thread_data = load_comment_thread_data()

  comments = extract_all_comments(comment_thread_data)

  with open("./data/comments/agg/comments.csv", "w") as fopen:
    dict_writer = DictWriter(fopen, fieldnames=comments[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(comments) 
