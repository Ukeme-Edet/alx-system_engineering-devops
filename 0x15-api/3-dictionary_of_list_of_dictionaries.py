#!/usr/bin/python3
"""
This script retrieves data from an API and saves it in a JSON file.
It fetches a list of users and their corresponding todos from the\
    JSONPlaceholder API.
The data is then transformed into a dictionary of lists of dictionaries, where\
    each user is a key and their todos are the values.
The resulting dictionary is then saved in a JSON file named\
    "todo_all_employees.json".
"""
import json
import requests

if __name__ == "__main__":
    with requests.Session() as s:
        base_url = "https://jsonplaceholder.typicode.com"
        users = s.get(f"{base_url}/users").json()
        with open("todo_all_employees.json", "w") as f:
            json.dump(
                {
                    user["id"]: [
                        {
                            "username": user["username"],
                            "task": todo["title"],
                            "completed": todo["completed"],
                        }
                        for todo in s.get(
                            f"{base_url}/users/{user['id']}/todos"
                        ).json()
                    ]
                    for user in users
                },
                f,
            )
