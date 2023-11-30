#!/bin/bash
# takes in a URL, sends a request displays the size
curl -sI -w "%{http_code}" "$1"
