# Overview #

## Background Context ##
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something ALX students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… [It actually powers 26% of the web](https://managewp.com/blog/statistics-about-wordpress-usage), so there is a fair chance that you will end up working with it at some point in your career. Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools. The web stack you are debugging today is a Wordpress website running on a LAMP stack.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

I love this!!!

*PS*
---
After completing this project on the third deadline, I must say that it is a very interesing one. I learned how to use tmux and strace ([see a substack I wrote here](https://))to troubleshoot a wordpress server. This project also gave me a deeper understanding of how wordpress works under the hood, boosting my confidence working with it.

---

## Folder Details ###
- **Date Created:** Sat. June 8 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Tue.June 4 2024 - 6am.
  - **1st Deadline:** Wed June 5 2024 - 6am.
  - **Duration:** 24 hrs.
  - **Month** 8, **Week** 1, **Day** 1


## General Requirements ##
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension

## Prerequisite Installations ##
### 1. Puppet-lint ###
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

#or

$ apt install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Reference Resources ##
- WebServer:
  - [Wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server)
  - [Web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)
  - [What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)
- [Troubleshooting a Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)
- [Troubleshooting Apache using strace](https://bobcares.com/blog/troubleshooting-apache-using-strace/)

## File Tree ##
.
├── 0-strace_is_your_friend.pp
└── README.md


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-strace_is_your_friend.pp](https://www.github.com/thecypherzen.com) | A puppet code that fixes server fail error.|
