#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    param = {"email": argv[2]}
    with urllib.parse.urlencode(param) as qeurystring:
        url = url + "?" + qeurystring
    with urllib.request.urlopen(url) as response:
        print(response.read())
