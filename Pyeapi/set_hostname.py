import pyeapi
import pprint

# Load device connection details from the eAPI configuration file
pyeapi.load_config("eapi.conf")

# Connect to the Arista switch named 'Arista1' as defined in eapi.conf
arista1 = pyeapi.connect_to('Arista1')

# Set the hostname of the switch to 'Arista1'
arista1.config('hostname Arista1')

# Run 'show hostname' command and pretty-print the result
pprint.pprint(arista1.enable('show hostname'))