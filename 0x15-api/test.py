#!/usr/bin/python3
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.json())
