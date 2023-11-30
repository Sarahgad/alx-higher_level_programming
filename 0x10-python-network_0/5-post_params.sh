#!/bin/bash
# takes in a URL, sends a request displays the size
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
