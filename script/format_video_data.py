#!/usr/bin/python3

from csv import DictWriter
import json

def load_video_data():
  with open("./data/videos/list.json", "r") as fopen:
    data = json.load(fopen)
  
  return data

def extract(data):
  return {
    "publishedAt": data.get("snippet", {}).get("publishedAt", ""),
    "channelId": data.get("snippet", {}).get("channelId", ""),
    "title": data.get("snippet", {}).get("title", ""),
    "description": data.get("snippet", {}).get("description", ""),
    "channelTitle": data.get("snippet", {}).get("channelTitle", ""),
    "tags": data.get("snippet", {}).get("tags", []),
    "categoryId": data.get("snippet", {}).get("categoryId", ""),
    "videoId": data.get("contentDetails", {}).get("videoId", ""),
    "duration": data.get("contentDetails", {}).get("duration", ""),
    "viewCount": data.get("contentDetails", {}).get("statistics", {}).get("viewCount", ""),
    "likeCount": data.get("contentDetails", {}).get("statistics", {}).get("likeCount", ""),
    "dislikeCount": data.get("contentDetails", {}).get("statistics", {}).get("dislikeCount", ""),
    "favoriteCount": data.get("contentDetails", {}).get("statistics", {}).get("favoriteCount", "")
  }

def extract_all(data):
  output = []

  for video in data:
    output.append(extract(video))
  
  return output

if __name__ == '__main__':
  video_data = load_video_data()

  videos = extract_all(video_data)

  with open("./data/videos/videos.csv", "w") as fopen:
    dict_writer = DictWriter(fopen, fieldnames=videos[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(videos) 
