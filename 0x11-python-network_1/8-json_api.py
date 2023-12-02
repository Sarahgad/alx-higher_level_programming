#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    response = requests.post(url=url, data=data)
    try:
        response_dict = response.json()
        if response_dict:
            print("[{}] {}".format(response_dict.get("id"), response_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
