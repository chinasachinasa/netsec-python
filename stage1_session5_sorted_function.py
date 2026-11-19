
devices = ["Router3", "Firewall1", "Switch1", "Router1"]

sorted_devices = sorted(devices)

print(sorted_devices)



devices = ["Router3", "Firewall1", "Switch1", "Router1"]

sorted_devices = sorted(devices, reverse=True)

print(sorted_devices)



#EXERCISE 1

network_devices1 = ["SW3", "R1", "FW1", "SW1", "R2", "FW2"]
sorted_devices1 = sorted(network_devices1)
print(sorted_devices1)


reverse_sorted_devices = ["SW3", "R1", "FW1", "SW1", "R2", "FW2"]
reverse_sorted_devices = sorted(network_devices1,reverse=True)
print(reverse_sorted_devices)