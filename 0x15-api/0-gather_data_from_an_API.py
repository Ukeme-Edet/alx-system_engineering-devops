#!/usr/bin/python3
"""
This script gathers data from an API and prints the tasks completed by an\
    employee.

Usage: python3 0-gather_data_from_an_API.py [employee_id]
"""

import requests
from sys import argv

if __name__ == "__main__":
    with requests.Session() as s:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
        todos = s.get(f"{url}/todos").json()
        user = s.get(url).json()
        done_todos = [todo for todo in todos if todo["completed"]]
        print(
            "Employee {} is done with tasks({}/{}):".format(
                user["name"], len(done_todos), len(todos)
            )
        )
        print(
            "\n".join([f"\t {done_todo['title']}" for done_todo in done_todos])
        )
