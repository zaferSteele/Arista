#!/usr/bin/python

# Description:
#   This script connects to an Arista switch using eAPI,
#   authenticates with the "enable" command using a secret password,
#   and retrieves the full running configuration in plain text format.
#
# Requirements:
#   - eAPI must be enabled on the Arista switch.
#   - jsonrpclib must be installed.
#   - Username: Zafer | Password: Steele | Enable password: SuperSecret
# -----------------------------------------------------------------------------

from jsonrpclib import Server

# Connect to the switch via eAPI on 192.168.255.3
switch = Server("https://Zafer:Steele@192.168.255.3/command-api")

# Run the "enable" command with password, then "show running-config"
response = switch.runCmds(
    1,
    [
        {"cmd": "enable", "input": "SuperSecret"},
        "show running-config"
    ],
    "text"  # Request the output in plain text format
)

# Print the running config output
print response[1]["output"]
