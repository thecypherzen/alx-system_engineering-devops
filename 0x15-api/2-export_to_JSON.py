#!/usr/bin/python3
"""A script that saves details of all tasks that are owned by an
     + employee and saves it in a json file

   Requirements:
   - must use urllib or requests module
   - must accept an integer as a parameter, which is the employee ID
   - the json file must be in the format:
        { "USER_ID": [
            {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
               "username": "USERNAME"},
            {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
               "username": "USERNAME"}, ... ]
        }
    - the filename must be <USER_ID>.json
"""

import json
import requests
import sys


if len(sys.argv) > 1:
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/" + \
        f"todos?userId={user_id}"

    # fetch todos
    todos = requests.get(url)
    if todos.status_code == requests.codes.ok:
        try:
            todos = todos.json()
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

            # parse json and print
            user_todos_list = []
            for todo in todos:
                current_todo = {"task": todo["title"], "completed":
                                todo["completed"], "username": username}
                user_todos_list.append(current_todo)
                todos_dict = {user_id: user_todos_list}

            with open(f"{user_id}.json", "w") as json_file:
                json.dump(todos_dict, json_file)
