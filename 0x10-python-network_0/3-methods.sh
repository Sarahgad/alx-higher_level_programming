#!/bin/bash
# takes in a URL, sends a request displays the size
curl -sI "$1" | grep -i "^Allow:"