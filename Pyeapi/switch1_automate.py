import switch_vlan_automation

# Create an instance of automate_switch using config file and device alias 'Arista1'
switch1 = switch_vlan_automation.automate_switch('eapi.conf', 'Arista1')

# Print the hostname retrieved from the Arista switch
print(switch1.hostname)

# Print the full running configuration of the switch
print(switch1.running_config)

# Create VLAN 10 and assign it the name 'vlan_created_using_automation'
print(switch1.create_vlan(10, 'vlan_created_using_automation'))

# Display all VLANs currently configured on the switch
print(switch1.node.api('vlans').getall())