#!/usr/bin/python3
"""A script that saves details of all tasks/todos of all users a json file

   Requirements:
   - must use urllib or requests module
   - must record all tasks from all employees
   - the json file must be in the format:
        { "USER_ID": [{"task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
          {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
               "username": "USERNAME"}, ... ],

          "USER_ID": [{"task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
              {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
              "username": "USERNAME"}, ... ], ...
        }
    - the filename must be todo_all_employees.json
"""

import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"

# fetch users
users_info = {}
users = requests.get(f"{base_url}/users")
if users.status_code == requests.codes.ok:
    try:
        users = users.json()
    except Exception:
        sys.exit(1)

# fetch todos for each user
for user in users:
    todos = requests.get(f"{base_url}/todos/?userId={user['id']}")
    if todos.status_code == requests.codes.ok:
        try:
            todos = todos.json()
        except Exception:
            sys.exit(1)

        # parse json and print
        user_todos_list = []
        for todo in todos:
            current_todo = {"task": todo["title"],
                            "completed": todo["completed"],
                            "username": user["username"]}
            user_todos_list.append(current_todo)
    users_info[f"{user['id']}"] = user_todos_list


with open("todo_all_employees.json", "w") as json_file:
    json.dump(users_info, json_file)
