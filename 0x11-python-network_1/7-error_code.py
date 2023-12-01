#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        response = requests.get(url=url)
        print(response.text)
    except requests.exceptions.HTTPError as error:
        print("Error code: {}".format(response.status_code))
