#!/bin/bash
# takes in a URL, sends a request displays the size
curl -s "$1" | wc -c
