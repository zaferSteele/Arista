import pyeapi
import pprint

# Load device connection details from the eAPI configuration file
pyeapi.load_config("eapi.conf")

# Connect to the Arista switch named 'Arista1' as defined in eapi.conf
arista1 = pyeapi.connect_to('Arista1')

# Execute 'show running-config' and store the full response
result = arista1.enable('show running-config')

# Extract and pretty-print the list of configuration commands under interface Ethernet1/3
pprint.pprint(result[0]['result']['cmds']['interface Ethernet1/3']['cmds'])