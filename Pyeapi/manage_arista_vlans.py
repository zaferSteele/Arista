import pyeapi
import pprint

# Load the configuration file for eAPI (includes connection info for Arista devices)
pyeapi.load_config("eapi.conf")

# Connect to the Arista switch defined as 'Arista1' in the config file
node = pyeapi.connect_to('Arista1')

# Access the VLANs API for interaction with VLAN configurations
vlans = node.api('vlans')

# Display available methods and attributes of the VLAN API object for inspection
pprint.pprint(dir(vlans))

# Retrieve and display all VLANs configured on the switch
pprint.pprint(vlans.getall())

# Retrieve and display details of VLAN ID 1
pprint.pprint(vlans.get(1))

# Create VLAN ID 5 if it does not already exist
pprint.pprint(vlans.create(5))

# Set a name for VLAN ID 5 to 'automate_creation_vlan'
pprint.pprint(vlans.set_name(5, 'automate_creation_vlan'))