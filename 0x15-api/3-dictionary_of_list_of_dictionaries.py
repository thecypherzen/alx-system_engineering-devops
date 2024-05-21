#!/usr/bin/python3
""" A script that uses the jsonplaceholder REST API, for a given
employee ID, to return all information on TODOS for all employees and
exports the data to json

Requirements:
    - 'urllib' or 'requests' module must be used
    - the script must display on stdout the information in this format:

      { "USER_ID": [
            {"username": "USERNAME", "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS},
            {"username": "USERNAME", "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS}, ...
            ],

           "USER_ID": [
           {"username": "USERNAME", "task": "TASK_TITLE",
           "completed": TASK_COMPLETED_STATUS},
           {"username": "USERNAME", "task": "TASK_TITLE",
           "completed": TASK_COMPLETED_STATUS}, ...
           ]
      }

   - File name must be: todo_all_employees.json
"""

if __name__ == "__main__":
    import json
    import requests

    uri = f"https://jsonplaceholder.typicode.com/users"
    all_users = {}

    # get user's name and todos
    users = list(requests.get(url=uri).json())
    for user in users:
        id = user.get("id", 0)
        if (id < 0 or id > 10):
            exit()
        tasks_list = []
        todos = requests.get(url=f"{uri}/{id}/todos")

        # calculate completed
        for item in list(todos.json()):
            tasks = (
                 ("username", user.get("username")),
                 ("task", item.get("title")),
                 ("completed", item.get("completed"))
            )
            tasks_list.append(dict(tasks))
        all_users[f"{id}"] = tasks_list
    with open("todo_all_employees.json", 'w') as f:
        json.dump(all_users, f)
