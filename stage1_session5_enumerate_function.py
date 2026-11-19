

devices = ["Router1", "Switch1", "Firewall1", "Router2"]

for index, device in enumerate(devices):
    print(index, device)


#Starting the count at 1
for index, device in enumerate(devices, start=1):
    print(index, device)


#exercise 1

network_devices = ["CORE-R1", "CORE-SW1", "BRANCH-R1", "BRANCH-SW1", "FIREWALL-1"]

for index,device in enumerate(network_devices,start = 1):
    print(index,device)