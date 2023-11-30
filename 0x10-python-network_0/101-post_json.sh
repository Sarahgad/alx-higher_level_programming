#!/bin/bash
# takes in a URL, sends a request displays the size
curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1"
