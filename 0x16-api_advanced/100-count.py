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
        response = sess.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("data").get("children")
            for i in range(len(data)):
                title = data[i].get("data").get("title").lower().split()
                for word in word_list:
                    if word.lower() in title:
                        word_count[word] = word_count.get(word, 0) + 1
            after = response.json().get("data").get("after")
            if after is not None:
                return count_words(subreddit, word_list, word_count, after)
            for word in sorted(word_list):
                if word_count.get(word) is not None:
                    print(f"{word}: {word_count.get(word)}")
            return
        if word_list == []:
            return
        print(None)
        return
