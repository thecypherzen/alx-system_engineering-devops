# Overview #
Telnet is a good way to connect to remote hosts using `telnet <IP> <PORT>. However, it's not at all times that we'd be able to connect remotely to a machine on a certain port, especially if it's blocked by the firewall.

Here, explore the usage of `ufw` to filter out unwanted traffic and or sources from accessing our network.

<hr/>

### Learning Objectives ###
- install and configure `ufw`
- set up ports forwarding on `ufw`
- what are iptables, rules and chains.

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
- **Date Created:** Mon. July 22, 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Mon. July 22, 2024 - 6am.
  - **1st Deadline:** Tue. July 23, 2024 - 6am.
  - **Duration:**  24hrs.


## Reference Resources
- [Web stack debugging](https://www.notion.so/WebStack-Debugging-ba8d7dd00b6042b898234b85b6a0eb1e)
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)


## Technologies ##
- OS: Ubuntu 20.04
- Vagrant
- Ubuntu Firewall (ufw)

## File Tree ##
ROOT
├── 0-block_all_incoming_traffic_but<br />
├── 100-port_forwarding<br />
└── README.md<br />

## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description/Task Details                                   |
|----|------|-----------------------------------------------|
| 1. | [0-block_all_incoming_traffic_but](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x13-firewall/0-block_all_incoming_traffic_but) | A file listing commands that:<br/>Configures `ufw` so that it blocks all incoming traffic, except the following TCP ports:<ul><li>22 (SSH)</li><li>443 (HTTPS SSL), and</li><li>80 (HTTP)</li></ul> |
| 2. | [100-port_forwarding](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x13-firewall/100-port_forwarding) | `ufw` confiruration forwarding port 8080/tcp to 80/tcp on a machine. |
| 3. | README.md | Project readme file |