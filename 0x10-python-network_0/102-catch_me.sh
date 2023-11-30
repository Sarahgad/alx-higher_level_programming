#!/bin/bash
# takes in a URL, sends a request displays the size
curl -s -w "%{http_code}:%{content_type}" 0.0.0.0:5000/catch_me
