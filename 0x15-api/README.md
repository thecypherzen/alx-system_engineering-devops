# Overview #
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so w're building and using Python scripts.

<hr/>

### Learning Objectives ###
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python


### Requirements and Constraints ###
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- Libraries imported in Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- Must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if __name__ == "__main__":)


## Folder Details ###
- **Date Created:** Mon. July 29, 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Mon. July 29, 2024 - 6am.
  - **1st Deadline:** Tue. July 30, 2024 - 6am.
  - **Duration:**  24hrs.


## Reference Resources
- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [What is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices](https://smartbear.com/learn/api-design/microservices/)
- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)


## File Tree ##
ROOT<br/>
├── 0-gather_data_from_an_API.py<br />
├── 1-export_to_CSV.py<br />
├── 2-export_to_JSON.py<br />
├── 3-dictionary_of_list_of_dictionaries.py<br />
├── README.md<br />
└── test.py<br />


## Files ###
*Here is a detailed list of all files in the repo and their description*.

| SN | File | Description/Task Details                                   |
|----|------|-----------------------------------------------|
| 1. | [0-gather_data_from_an_API.py ](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x15-api/0-gather_data_from_an_API.py) | A Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress, in this format:<br/>*First line: Employee `EMPLOYEE_NAME` is done with tasks(`NUMBER_OF_DONE_TASKS`/`TOTAL_NUMBER_OF_TASKS`):*<br/>Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tab character and 1 space before the `TASK_TITLE`). |
| 2. | [1-export_to_CSV.py](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x15-api/1-export_to_CSV.py) | A python script that records a user's todos progress information in a `csv` file. The `.csv` file is in the format: `"<USER_ID>"`,`"<USERNAME>"`,`"<TASK_COMPLETED_STATUS">`,`"<TASK_TITLE>"`; and named as `<USER_ID>`.csv. |
| 3. | [2-export_to_JSON.py](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x15-api/2-export_to_JSON.py) | A script that saes all tasks owned by an employee in a json file, named `<USER_ID>.json`.The file is formatted as: *{ `"<USER_ID>"`: [{"task": `"<TASK_TITLE>"`, "completed": `<TASK_COMPLETED_STATUS>`, "username": `"<USERNAME>"`}, {"task": `"<TASK_TITLE>"`, "completed": `<TASK_COMPLETED_STATUS>`, "username": `"<USERNAME>"`}, ... ]}*  |
| 4. | [3-dictionary_of_list_of_dictionaries.py](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x15-api/3-dictionary_of_list_of_dictionaries.py) | A script that saves information of tasks for all employees in a file named `todo_all_employees.json`, and formatted as 3 above. |
| 5. | README.md | Folder readme |
| 6. | [test.py]() | A script for simple testing of commands before execution |