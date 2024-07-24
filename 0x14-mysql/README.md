# Overview #
When building a web infrastructure, it is important to take high availability seriously. In addition to the web-server itself, the database also has to be available at all times, regardless of downtimes.

This project is therefore, all about ensuring database high-availability through replication.

<hr/>

### Learning Objectives ###
At the completion of this project, we should be conversant with the following:
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should be regularly performed to make sure that your database backup strategy actually works



### Requirements and Constraints ###
- Allowed editors: `vi`, `vim`, and `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing


## Folder Details ###
- **Date Created:** Tue. July 23, 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Tue. July 23, 2024 - 6am.
  - **1st Deadline:** Wed. July 24, 2024 - 6am.
  - **Duration:**  24hrs.


## Reference Resources
- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)
- [mysqldump](https://linux.die.net/man/1/mysqldump)



## File Tree ##
ROOT<br/>
├── 0-block_all_incoming_traffic_but<br />
├── 100-port_forwarding<br />
└── README.md<br />



## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description/Task Details                                   |
|----|------|-----------------------------------------------|
| 1. | [4-mysql_configuration_primary]() | Task 4, file 1 |
| 2. | [4-mysql_configuration_replica]() | Task 4 file 2 |