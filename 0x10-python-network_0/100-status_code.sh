#!/bin/bash
# takes in a URL, sends a request displays the size
curl -s -o /dev/null -w "%{http_code}" "$1"
