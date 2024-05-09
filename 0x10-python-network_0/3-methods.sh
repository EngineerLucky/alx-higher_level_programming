#!/bin/bash
# A bash script that takes UR Land Displays all HTTP methods the server will accept.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
