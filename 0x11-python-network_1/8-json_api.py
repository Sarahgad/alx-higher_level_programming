#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if argv[1] == None:
        data = {'q': ""}
    else:
        data = {'q': argv[1]}
    response = requests.post(url=url, data=data)
    if not response.json():
        print("Not a valid JSON")
    else:
        response_dict = response.json()
        id = response_dict['id']
        name = response_dict['name']
        if id and name:
            print("[{}] {}".format(id, name))
        else:
            print("No result")
