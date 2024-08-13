#!/usr/bin/python3
"""
This script counts the occurrences of words from a given word list in the\
    titles of the hot posts of a subreddit.
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Count the occurrences of words from a given word list in the titles of the\
        hot posts of a subreddit.

    Args:
            subreddit (str): The name of the subreddit.
            word_list (list): A list of words to count.
            word_count (dict): A dictionary to store the word counts (default\
                {}).
            after (str): The "after" parameter for pagination (default None).

    Returns:
            None
    """
    with requests.Session() as sess:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {"limit": 100, "after": after}
        response = sess.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json().get("data").get("children")
            for i in range(len(data)):
                title = data[i].get("data").get("title").lower().split()
                for word in word_list:
                    word_count[word] = word_count.get(word, 0) + title.count(
                        word
                    )
            after = response.json().get("data").get("after")
            if after is not None:
                return count_words(subreddit, word_list, word_count, after)
            if len(word_count) == 0:
                return None
            for key in sorted(word_count, key=word_count.get, reverse=True):
                if word_count[key] > 0:
                    print(f"{key}: {word_count[key]}")
        else:
            return None
