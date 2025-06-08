import pyeapi

class automate_switch():
    
    def __init__(self, config_file_location, device):
        # Load eAPI config file to set up available devices and credentials
        pyeapi.client.load_config(config_file_location)
        
        # Establish connection to the specified device from config
        self.node = pyeapi.connect_to(device)
        
        # Retrieve and store the device's hostname for reference
        self.hostname = self.node.enable('show hostname')[0]['result']['hostname']
        
        # Retrieve and store the running configuration for the device
        self.running_config = self.node.enable('show running-config')
    
    def create_vlan(self, vlan_number, vlan_name):
        # Access the VLAN API for this node to perform VLAN operations
        vlans = self.node.api('vlans')
        
        # Create a VLAN with the given number (no-op if it already exists)
        vlans.create(vlan_number)
        
        # Assign a name to the newly created or existing VLAN
        vlans.set_name(vlan_number, vlan_name)