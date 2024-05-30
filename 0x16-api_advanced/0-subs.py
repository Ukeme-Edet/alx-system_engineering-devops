#!/usr/bin/python3
"""
This module contains a function to retrieve the number of subscribers for a\
    given subreddit.
"""
import requests

headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Modhash": f"{requests.get("https://www.reddit.com/api/me.json").json().get("data").get("modhash")}",
}


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
            subreddit (str): The name of the subreddit.

    Returns:
            int: The number of subscribers for the subreddit.
    """
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


print(number_of_subscribers("programming"))
print(number_of_subscribers("this_is_a_fake_subreddit"))
