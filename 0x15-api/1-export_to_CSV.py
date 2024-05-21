#!/usr/bin/python3
""" A script that uses the jsonplaceholder REST API, for a given
employee ID, to return information about a TODO list progress.

Requirements:
    - 'urllib' or 'requests' module must be used
    - the script must accept an integer as a parameter, which is the
      + employee ID
    - the script must display on the standard output the employee TODO list
      progress in this exact format:

      First line: Employee EMPLOYEE_NAME is done with
                  tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

      where:
          EMPLOYEE_NAME: name of the employee
          NUMBER_OF_DONE_TASKS: number of completed tasks
          TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
          + completed and non-completed tasks
      Second and N next lines display the title of completed tasks:
      + TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        if id < 1 or id > 10:
            exit()
        uri = f"https://jsonplaceholder.typicode.com/users/{id}"
        completed = 0
        total = 0
        completed_list = []

        # get user's name and todos
        user = requests.get(url=uri)
        name = dict(user.json()).get("name", "None")
        todos = requests.get(url=f"{uri}/todos")

        # calculate completed
        for item in list(todos.json()):
            total += 1
            is_completed = item.get("completed", False)
            if is_completed:
                completed += 1
                completed_list.append(item.get("title"))
        msg = f"Employee {name} is done with tasks({completed}/{total}):"
        for todo in completed_list:
            msg += f"\n\t {todo}"
        print(msg)
