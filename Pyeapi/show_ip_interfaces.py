import pyeapi
import pprint

# Load connection settings from the eAPI config file
pyeapi.load_config("eapi.conf")

# Establish a connection to the device named 'Arista1' as defined in eapi.conf
arista1 = pyeapi.connect_to('Arista1')

# Run 'show ip interface brief' command and pretty-print the output
pprint.pprint(arista1.enable('show ip interface brief'))