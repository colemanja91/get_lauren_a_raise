#!/usr/bin/python3

from youtube import youtube

client = youtube()

def get_channel_id():
  channel = client.channels().list(
    part="contentDetails",
    id="UC6MnY4d56I8j2H327vZzmFg"
  ).execute()

  print(channel)

if __name__ == '__main__':
  get_channel_id()
