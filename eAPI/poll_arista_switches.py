#!/usr/bin/python
# Description:
#   This script connects to a rack of Arista switches using eAPI (10.0.0.1 to 10.0.0.10),
#   retrieves the system MAC address, software version, and architecture of each switch,
#   and prints the collected information in a formatted table.
#
# Requirements:
#   - Arista switches must have eAPI enabled.
#   - jsonrpclib must be installed.
#   - Username: Zafer | Password: Steele
# -----------------------------------------------------------------------------

from jsonrpclib import Server

print "Switch#   System Mac         Version  Architecture"
print "--------------------------------------------------"

for x in range(1, 11):
    x = str(x)

    switch = Server("https://Zafer:Steele@10.0.0." + x + "/command-api")
    response = switch.runCmds(1, ["show version"])

    print "Switch-" + x.ljust(3) + \
          response[0]["systemMacAddress"].ljust(19) + \
          response[0]["version"].ljust(9) + \
          response[0]["architecture"]
