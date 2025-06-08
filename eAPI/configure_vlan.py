#!/usr/bin/python3

# Ensure Python 3-style print function in Python 2 (has no effect in Python 3)
from __future__ import print_function

# Import JSON-RPC client and utility modules
from jsonrpclib import Server
import ssl, pprint

# Disable SSL certificate verification (for self-signed certs; insecure for production use)
ssl._create_default_https_context = ssl._create_unverified_context

# Function to send a list of CLI commands to an Arista switch via eAPI
def runAristaCommands(switch_object, list_of_commands):
    response = switch_object.runCmds(1, list_of_commands)  # Use eAPI version 1
    return response

# Connect to Arista switch using JSON-RPC over HTTP with basic authentication
# Replace Script with your EAPI username and Arista with your EAPI password
# Replace the IP address with your EAPI IP address
switch = Server("http://Script:Arista@192.168.255.100/command-api")

# Define CLI commands to configure interface Ethernet 3 with VLAN 100 and save config
commands = [
    'enable',
    'configure',
    'interface ethernet 3',
    'switchport access vlan 100',
    'end',
    'write memory'
]

# Send commands and capture the response
response = runAristaCommands(switch, commands)

# Pretty-print the response from the switch
pprint.pprint(response)