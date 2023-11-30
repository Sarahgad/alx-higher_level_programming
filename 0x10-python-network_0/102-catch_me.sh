#!/bin/bash
# takes in a URL, sends a request displays the size
curl -s -X PUT "0.0.0.0:5000/catch_me" | grep -o "You got me!"
