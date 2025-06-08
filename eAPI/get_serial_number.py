#!/usr/bin/python3

# Enable Python 3 print function behavior in Python 2 (no effect in Python 3)
from __future__ import print_function

# Import the JSON-RPC client library
from jsonrpclib import Server

# Import SSL module to modify SSL context behavior
import ssl

# Disable SSL certificate verification (useful for self-signed certs; not recommended for production)
ssl.create_default_context = ssl._create_unverified_context

# Connect to the Arista switch using JSON-RPC over HTTP with basic auth
# Replace Script with your EAPI username and Arista with your EAPI password
# Replace the IP address with your EAPI IP address

switch = Server("http://Script:Arista@192.168.255.100/command-api")

# Send 'show version' command using API version 1
response = switch.runCmds(1, ["show version"])

# Extract and print the serial number from the command response
print('Serial Number: ' + response[0]['serialNumber'])