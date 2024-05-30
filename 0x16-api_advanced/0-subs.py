#!/usr/bin/python3
"""
This module contains a function to retrieve the number of subscribers for a\
    given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
            subreddit (str): The name of the subreddit.

    Returns:
            int: The number of subscribers for the subreddit.
    """
    with requests.Session() as sess:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            return (
                sess.get(url, headers=headers)
                .json()
                .get("data")
                .get("subscribers")
            )
        except Exception:
            return 0
