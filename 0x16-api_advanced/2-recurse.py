#!/usr/bin/python3
"""
This script returns a list containing the titles of all hot articles for a\
    given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None):
    """
    Recursively retrieves all hot articles for a given subreddit.

    Args:
            subreddit (str): The name of the subreddit.
            hot_list (list): A list to store the titles of hot articles.

    Returns:
            list: A list containing the titles of all hot articles for a given\
                subreddit.
    """
    hot_list = hot_list if hot_list is not None else []
    with requests.Session() as sess:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = sess.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("data").get("children")
            for i in range(len(data)):
                hot_list.append(data[i].get("data").get("title"))
            after = response.json().get("data").get("after")
            if after is not None:
                return recurse(subreddit, hot_list)
            return hot_list
        return None
