#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    basic = HTTPBasicAuth(argv[1], argv[2])

    response = requests.get(url=url, auth=basic)
    print(response.json().get('id'))
