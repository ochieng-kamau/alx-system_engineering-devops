#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyRedditBot/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

