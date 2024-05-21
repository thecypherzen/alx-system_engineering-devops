#!/usr/bin/python3
""" A script that uses the jsonplaceholder REST API, for a given
employee ID, to return information about a TODO list progress and
exports the data to json

Requirements:
    - 'urllib' or 'requests' module must be used
    - the script must accept an integer as a parameter, which is the
      + employee ID
    - the script must display on the standard output the employee TODO list
      progress in this exact format:

      { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,\
      "username": "USERNAME"}, {"task": "TASK_TITLE", "completed":\
      TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

      where:
          USER_ID: id of user
          TASK_TITLE: title of user's task
          TASK_COMPLETED_STATUS: status of task
          USERNAME: user's username

   - File name must be: USER_ID.json
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        if id < 1 or id > 10:
            exit()
        uri = f"https://jsonplaceholder.typicode.com/users/{id}"
        completed = 0
        total = 0
        tasks_list = []

        # get user's name and todos
        user = dict(requests.get(url=uri).json())
        todos = requests.get(url=f"{uri}/todos")

        # calculate completed
        for item in list(todos.json()):
            tasks = (
                ("task", item.get("title")),
                ("completed", item.get("completed")),
                ("username", user.get("username"))
            )
            tasks_list.append(dict(tasks))
        msg = {f"{id}": tasks_list}
        with open(f"{id}.json", 'w') as f:
            json.dump(msg, f)
