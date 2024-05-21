#!/usr/bin/python3
""" A script that uses the jsonplaceholder REST API, for a given
employee ID, to return information about a TODO list progress and
exports the data to csv

Requirements:
    - 'urllib' or 'requests' module must be used
    - the script must accept an integer as a parameter, which is the
      + employee ID
    - the script must display on the standard output the employee TODO list
      progress in this exact format:

      "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

      where:
          USER_ID: id of user
          USERNAME: username
          TASK_COMPLETED_STATUS: completed status of task
          TASK_TITLE: title of task

    - File name must be: USER_ID.csv
"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        if id < 1 or id > 10:
            exit()

        uri = f"https://jsonplaceholder.typicode.com/users/{id}"
        # get user's name and todos
        user = dict(requests.get(url=uri).json())
        todos = requests.get(url=f"{uri}/todos")
        rows = []

        # calculate completed
        for item in list(todos.json()):
            rows.append([
                f"{id}",
                f"{user.get('username')}",
                f"{item.get('completed')}",
                f"{item.get('title')}"
                ])
        with open(f"{id}.csv", 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(rows)
