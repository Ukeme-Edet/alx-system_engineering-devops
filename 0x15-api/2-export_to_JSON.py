#!/usr/bin/python3
"""
This script exports a user's TODO list data from the JSONPlaceholder API to a\
    JSON file.

The script takes a user ID as a command-line argument and retrieves the user's\
    TODO list and user information from the JSONPlaceholder API.
It then saves the data in a JSON file named after the user ID.

Example usage:
    $ python3 2-export_to_JSON.py 1

This will retrieve the TODO list and user information for user with ID 1 and\
    save it in a file named "1.json".
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    with requests.Session() as s:
        user_id = argv[1]
        res = s.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        ).json()
        user = s.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        ).json()
        with open(f"{user_id}.json", "w") as f:
            json.dump(
                {
                    user_id: [
                        {
                            "task": todo["title"],
                            "completed": todo["completed"],
                            "username": user["username"],
                        }
                        for todo in res
                    ]
                },
                f,
            )
