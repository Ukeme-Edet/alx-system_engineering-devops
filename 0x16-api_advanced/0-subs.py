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
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0",
            "Authorization": "JrMqC76IDb69XbfxT2Tes_cVx1rAkg",
        }
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = session.get(url, allow_redirects=False)
        if response.status_code == 404:
            return 0
        return response.json().get("data").get("subscribers")
