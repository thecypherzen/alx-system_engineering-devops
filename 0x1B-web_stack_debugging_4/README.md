# Overview #

## Background Context ##
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using [ApacheBench](https://httpd.apache.org/docs/current/programs/ab.html) which is a quite popular tool in the industry. It allows us to simulate HTTP requests to a web server. For starters, we have a serverto which we  made 2000 requests with 100 requests at a time. 696 requests failed - this may vary from time to time, but it's still bad because if 700/2000 requests are failing, it translates to 35% of our users complaining! Our first task is to  fix our stack so that we get failures down to 0, using our Werkzeugsatz - *German for toolkit* 💪💪🧰


In second scenaria, we are prensented with a server which has a user *holberton*. However, when `su - holberton` is attempted, the error `-su: /home/holberton/.bash_profile: Too many open files` pops up. Our task is to resolve this issue and write a puppet manifest to automate it. Nice 😎🤩


## Folder Details ###
- **Date Created:** Thur Aug 22 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Mon Aug 19 2024 - 6am.
  - **1st Deadline:** Fri Aug 23 2024 - 6am.
  - **Duration:** 96hrs(4days).<br/>


## Requirements ##
### General ###
- All are interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension .pp
- Files will be checked with Puppet v3.4

### Install puppet-lint ###
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File                         | Description                                         |
|----|------------------------------|-----------------------------------------------------|
| 1. | [0-the_sky_is_the_limit_not.pp](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x1B-web_stack_debugging_4/0-the_sky_is_the_limit_not.pp) | A puppet manifest that raises the limit on concurrent nginx open files.|
| 2. | [1-user_limit.pp](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x1B-web_stack_debugging_4/1-user_limit.pp) | A puppet manifest that raises the limit on user `holberton`'s simultaneous open files.|
