#!/usr/bin/python3
"""
This script retrieves the top ten posts from a specified subreddit on Reddit.
"""

import requests


def top_ten(subreddit):
    """
    Retrieves the top ten posts from a specified subreddit on Reddit.

    Args:
            subreddit (str): The name of the subreddit.

    Returns:
            None
    """
    with requests.Session() as sess:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = sess.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("data").get("children")
            for i in range(10):
                print(data[i].get("data").get("title"))
        else:
            print(None)
