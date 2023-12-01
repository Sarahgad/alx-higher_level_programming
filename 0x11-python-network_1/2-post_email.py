#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    param = {"email": argv[2]}
    qeurystring = urllib.parse.urlencode(param).encode('utf-8')
    request = urllib.request.Request(url=url, data=param, method='post')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
