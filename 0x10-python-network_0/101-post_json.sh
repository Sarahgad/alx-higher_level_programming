#!/bin/bash
# takes in a URL, sends a request displays the size
curl -s -X POST -H "$2" "$1"
