# Overview #
**Web stack debugging #0** is the first project in the webstack debugging series. The Webstack debugging series focuses on the art of debugging.

Computers and software rarely work the way we want (that’s the “fun” part of the job!). Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks are given, and the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, we should figure out what is going on and fix it manually.

**Web stack debugging #0** therefore, is the first manual step on this journey.


<hr />

## Background Context ##
In this first debugging project, you will need to get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it.
```
$ docker run -p 8080:80 -d -it holbertonschool/265-0
$ docker ps

# we can see that the image is downloaded and running
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla

$ curl 0:8080
curl: (56) Recv failure: Connection reset by peer

$ curl -v 0:8080
*   Trying 0.0.0.0:8080...
* TCP_NODELAY set
* Connected to 0 (127.0.0.1) port 8080 (#0)
> GET / HTTP/1.1
> Host: 0:8080
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Recv failure: Connection reset by peer
* Closing connection 0
curl: (56) Recv failure: Connection reset by peer

```

From this, we can see that the server is failing.

## Mission ##
After connecting to the container and fixing whatever needed to be fixed, Paste the command(s) you used to fix the issue in the answer file.


## Folder Details ###
- **Date Created:** Sat. July 13 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Mon. July 1, 2024 - 6am.
  - **1st Deadline:** Wed. July 3 2024 - 6am.
  - **Duration:** 48hrs (2 days).
  - **Month** 5, **Week** 4, **Day** 2.



## Requirements ##
### General ###
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing


## Resources ##
- [Network basics](https://www.notion.so/Network-Basics-a8893442be654f3a9f7d5f2f4fceb3d7)
- [Docker](https://www.notion.so/Docker-24b44127a9d4411680a7c8b74e5d1b0a)
- [Web stack debugging](https://www.notion.so/WebStack-Debugging-ba8d7dd00b6042b898234b85b6a0eb1e)
- [`curl` Manual](https://curl.se/docs/manpage.html)


## Dependencies to Install ##
### Docker ###
- [Mac OS](https://docs.docker.com/desktop/install/mac-install/)
- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Ubuntu 14.04](https://www.liquidweb.com/blog/how-to-install-docker-on-ubuntu-14-04-lts/) *(Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)*
- [Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

## File Tree ##
pending


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-give_me_a_page](https://www.github.com) |  |
