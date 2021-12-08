#!/usr/bin/python3

from os import environ
from googleapiclient.discovery import build

api_key = environ["YT_API_KEY"]

def youtube():
  return build('youtube', 'v3', developerKey=api_key)
