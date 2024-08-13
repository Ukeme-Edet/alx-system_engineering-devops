#!/usr/bin/python3
"""
This module contains a function to retrieve the number of subscribers for a\
    given subreddit.

Functions:
- number_of_subscribers(subreddit): Retrieves the number of subscribers for a\
    given subreddit.

"""


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
            subreddit (str): The name of the subreddit.

    Returns:
            int: The number of subscribers for the subreddit. Returns 0 if the\
                subreddit does not exist or if there was an error in the\
                    request.
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
