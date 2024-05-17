#!/usr/bin/python3
"""
This script exports user's TODO list from a given user ID to a CSV file.
It uses the jsonplaceholder API to retrieve the user's TODO list and user\
    information.
The script takes the user ID as a command-line argument and generates a CSV\
    file named after the user ID.
The CSV file contains the user ID, username, completion status, and title of\
    each TODO item.
"""
import csv
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
        with open(f"{user_id}.csv", "w") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            [
                writer.writerow(
                    [
                        user_id,
                        user["username"],
                        todo["completed"],
                        todo["title"],
                    ]
                )
                for todo in res
            ]
