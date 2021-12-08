# Get Lauren a Raise (PointCrow Clips)

Data analysis of the YouTube "PointCrow Clips" channel illustrating
engagement over time relative to community efforts to get Lauren
(editor, channel manager) a raise.

Only data publicly-available over the YouTube APIs is used. 

## Prerequisites

- YouTube API Key
  + This is a good guide: https://www.geeksforgeeks.org/youtube-data-api-set-1/
  + In this repo, the key is assumed to be the environment variable `YT_API_KEY`
- Python3 requirements
  + `pip install -r requirements.txt`
  + Recommended using `virtualenv`

## Overview

- `data/`
  + Output data from the scripts being run in this repo
- `script/`
  + Python scripts which pull data from the YT API

## Get the channel ID

**TL;DR**
+ The channel ID is `UC6MnY4d56I8j2H327vZzmFg`

```
python3 ./script/get_channel_id
```

## Get list of channel videos

- Output stored in `data/videos/list.json`

## Get all video comments

- Raw output stored in `data/comments/raw/comment_threads.json`

## Aggregate all comments to a CSV file

- Output stored in `data/comments/agg/comments.csv`

## Actual analyses

SQL scripts stored in `sql/`. DB is assumed to be PostgreSQL.

### Comment Volume

- total comments
- Total parent comments
- Total threads with replies
- What are the most-liked comments?
- What is the most-commented video?
- Which comment thread has the most engagement?
- Which video is most disliked?
- Any correlation between duration and performance?

### Raise

- When did the first raise-related comment appear?
  + Before or after the initial clip?
- Did anyone retroactively comment about the raise on older clips?
- Who has commented the most about the raise?
- Did the raise produce a noticeable increase in comment-based engagement?

### Laid

- Same as raise, but for getting laid
