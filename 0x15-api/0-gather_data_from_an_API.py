#!/usr/bin/python3
"""A script that uses json placeholder api to fetch a user's
     information by id

   Requirements:
   - must use urllib or requests module
   - must accept an integer as a parameter, which is the employee ID
   - must display on the standard output the employee TODO list
     +progress in this exact format:
     => First line: Employee <EMPLOYEE_NAME> is done with
        +tasks(<NUMBER_OF_DONE_TASKS>/<TOTAL_NUMBER_OF_TASKS>):

        WHERE:
        - EMPLOYEE_NAME => name of the employee
        - NUMBER_OF_DONE_TASKS => number of completed tasks
        - TOTAL_NUMBER_OF_TASKS => total number of tasks, which is the
           +sum of completed and non-completed tasks
     => Second and N next lines display the title of completed tasks:
         +<TASK_TITLE> (with 1 tab and 1 space before the TASK_TITLE)
"""

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
            completed = [todo for todo in todos if todo['completed']]
        except Exception:
            sys.exit(1)

        # fetch user info
        url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
        user = requests.get(url)
        if user.status_code == requests.codes.ok:
            try:
                name = user.json()["name"]
            except Exception:
                sys.exit(1)

            # parse message and print
            count = len(completed)
            message = f"Employee {name} is done " + \
                f"with tasks({count}/{len(todos)}):\n"
            for todo in completed:
                count -= 1
                message += f"\t {todo['title']}"
                if count:
                    message += '\n'
            print(message)
