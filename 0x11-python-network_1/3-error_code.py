#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    request = urllib.request.Request(url=url)
    with urllib.request.urlopen(request) as response:
        try:
            print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as error:
            print(error.status)
