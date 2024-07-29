#!/usr/bin/python3
"""A script that records a user's todo info from json placeholder
    + and exports to csv

   Requirements:
   - must use urllib or requests module
   - must accept an integer as a parameter, which is the employee ID
   - file is formatted in this order:
       <"USER_ID">,<"USERNAME">,<"TASK_COMPLETED_STATUS">,<"TASK_TITLE">
"""

import csv
import requests
import sys


if len(sys.argv) > 1:
    url = "https://jsonplaceholder.typicode.com/" + \
        f"todos?userId={sys.argv[1]}"

    # fetch todos
    todos = requests.get(url)
    if todos.status_code == requests.codes.ok:
        try:
            todos = todos.json()
            user_id = todos[0]["userId"]
        except Exception:
            sys.exit(1)

        # fetch user info
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user = requests.get(url)
        if user.status_code == requests.codes.ok:
            try:
                username = user.json()["username"]
            except Exception:
                sys.exit(1)

            # parse content to csv file
            with open(f"{user_id}.csv", "w", newline="") as user_csv:
                writer = csv.writer(user_csv, delimiter=",",
                                    quotechar='"', quoting=csv.QUOTE_ALL)
                for todo in todos:
                    writer.writerow([user_id, username, todo["completed"],
                                     todo["title"]])
