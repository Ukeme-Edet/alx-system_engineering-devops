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
    mh_url = "https://www.reddit.com/api/me.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    headers["X-Modhash"] = (
        requests.get(mh_url, headers=headers).json().get("data").get("modhash")
    )
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    with requests.Session() as sess:
        try:
            return (
                sess.get(url, headers=headers)
                .json()
                .get("data")
                .get("subscribers")
            )
        except Exception:
            return 0
