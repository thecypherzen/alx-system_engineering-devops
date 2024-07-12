# Overview #

HTTPS is necessary today for security and public trust. But as an engineer, how do we set it up on our web infrsastructure? This is what the *0x10. HTTPS SSL* focuses on.

<hr/>

### Learning Objectives ###
- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

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
- **Date Created:** Thur. July 11, 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Thur July 11, 2024 - 6am.
  - **1st Deadline:** Fri July 12, 2024 - 6am.
  - **Duration:**  24hrs.


## Reference Resources
- [DNS](https://www.notion.so/DNS-cfbd9d6ce4c7433698666d27be76d9bb)
- [Web stack debugging](https://www.notion.so/WebStack-Debugging-ba8d7dd00b6042b898234b85b6a0eb1e)
- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/getting-started/basic-tutorials)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)


## Technologies ##
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- Code tested on Ubuntu 20.04 LTS.

## File Tree ##
├── 0-world_wide_web<br/>
├── 1-haproxy_ssl_termination<br/>
├── 100-redirect_http_to_https<br/>
└── README.md<br/>


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description/Task Details                                   |
|----|------|-----------------------------------------------|
| 1. | [0-world_wide_web](https://https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x10-https_ssl/0-world_wide_web) | A bash script that displays information about the subdomains of a given domain.<br/>**Preamble**<br/>Configure `ridgesolid.tech` domain zone so that the subdomain `www` points to the load-balancer IP (lb-01).<br/>**Requirements**<br/><ul>Add the subdomain `www` to the domain, and point it to the lb-01's IP</li><li>Add the subdomain lb-01 to your domain, point it to your lb-01 IP</li><li>Add the subdomain web-01 to your domain, point it to your web-01 IP</li><li>Add the subdomain web-02 to your domain, point it to your web-02's IP.</li><li>The Bash script must accept 2 arguments:<br/><ol><li>`domain`:<ul><li>**type**: string</li><li>**what**: domain name to audit</li><li>**mandatory**: yes</li></ul></li><li>`subdomain`:<ul><li>**type**: string</li><li>**what**: specific subdomain to audit</li><li>**mandatory**: no</li></ul></li></ol></li><li>**Output**: *The subdomain `[SUB_DOMAIN]` is a `[RECORD_TYPE]` record and points to `[DESTINATION]`*</li><li>When only the parameter domain is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order</li><li>When passing domain and subdomain parameters, display information for the specified subdomain</li><li>Ignore `shellcheck` case `SC2086`</li><li>**Must use**:<ul><li>awk, and</li><li>at least one Bash function</li><ul><li>No need to handle edge cases such as:<ul><li>Empty parameters</li><li>Nonexistent domain names</li><li>Nonexistent subdomains</li></ul></ul> |
| 2. | [1-haproxy_ssl_termination](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x10-https_ssl/1-haproxy_ssl_termination) | **Preamble**<br/>“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination. Create a certificate using `certbot` and configure HAproxy to accept encrypted traffic for your subdomain `www`. This file is the haproxy configuration file that meets the folliwing specifications.**Requirements**:<br/><ul><li>HAproxy must be listening on port TCP 443</li><li>HAproxy must be accepting SSL traffic</li><li>HAproxy must serve encrypted traffic that will return the `/` of your web server</li><li>When querying the root of your domain name, the page returned must contain `Holberton School`.</li></ul> |
| 3. | [100-redirect_http_to_https](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x10-https_ssl/100-redirect_http_to_https)  | An `haproxy` configuration file that enforces https requests.<br/>**Requirements**:<ul><li>This should be transparent to the user</li><li>HAproxy should return a `301`</li><li>HAproxy should redirect HTTP traffic to HTTPS</li></ul>  |