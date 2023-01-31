#!/usr/bin/python3
"""
Requests module for sending HTTP requests to the Reddit API
"""
import requests


def top_ten(subreddit):
    """Return the top 10 hot posts on a given subreddit."""
    headers = {'User-Agent': 'MyRedditBot/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            # subscribers = data['data']['subscribers']
            print(post['data']['title'])
    else:
        print(None)
