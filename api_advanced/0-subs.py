#!/usr/bin/python3
"""
This is a function that queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit
"""

import json
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit
    """
    subreddit_URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(subreddit_URL, headers={"user-agent": "user"}, allow_redirects=False)
    if response.status_code == 200:
        print("OK", end='')
        subreddit_info = response.json()
        if "data" in subreddit_info:
            children = subreddit_info.get("data").get("children")
            for child in children:
                print(child.get("data").get("title"))
    else:
        print("Not a valid subreddit", end='')
