devices = ["R1", "R2", "SW1", "SW2", "FW1"]

for device in devices:
    print(device)
print("Monitoring completed")


routers = ["R1", "R2", "R3",]
for router in routers:
    print("checking:",router)
print("All Network devices have been checked")



#PRACTICAL EXERCISE 1

# 1. Create the list called devices
devices = ["R1", "R2", "SW1", "SW2", "FW1"]

# 2 & 3. Write a for loop using 'device' as your loop variable
for device in devices:
    # 4. Print 'Checking network device:' followed by the device name (inside the loop)
    print(f"Checking network device: {device}")

# 5. Print 'Monitoring completed.' outside the loop (no indentation)
print("Monitoring completed.")


#EXERCISE 2
print("Network Inventory Report")
print("-" * 30)
network_devices = ["R1", "R2", "SW1", "SW2", "FW1"]
for device in network_devices:
    print(f"Device registered: {device}")
print("-" * 30)
print("Total inventory processed.")


#RANGE FUNCTION
# 1. Use the range function to print numbers from 0 to 4
for number in range(5):
    print(number)


for number1 in range(1, 6):
    print(number1)


for attempt in range(1, 4):
    print(f"Connectivity test {attempt}")



#EXERCISE 3

device_name="BR1-R1"
print(f"Starting connectivity tests for {device_name}")
print("-" * 32)

for attempt in range(1,6):
    print(f"Connectivity test attempt :{attempt}")

print("-" * 32)
print("Connectivity testing completed")


#for loops with dictionaries

router1 = {
    "hostname": "BR1-R1",
    "ip_address": "192.168.10.1",
    "status": "Online"
}
for key in router1:
    print(key)

for value in router1.values():
    print(value)

#we use .item() to print both keys and vlaues and .key() for keys and .value() for values

for key, value in router1.items():
    print(f"{key}: {value}")




print("NETWORK DEVICE INVENTORY")
print("-" *32)

switch = {
    "hostname": "BR2-SW1",
    "ip_address": "192.168.20.2",
    "device_type": "Layer 2 Switch",
    "status": "Online",
    "location": "Branch 2"
}


for key,value in switch.items():
    print(f"{key}: {value}")

print("-" * 32)
print("Inventory report completed.")


#Iterating through a list of dictionaries

devices1 = [
    {
        "hostname": "BR1-R1",
        "ip_address": "192.168.10.1",
        "status": "Online"
    },
    {
        "hostname": "BR2-SW1",
        "ip_address": "192.168.20.2",
        "status": "Online"
    },
    {
        "hostname": "HQ-FW1",
        "ip_address": "192.168.1.254",
        "status": "Offline"
    }
]

for device in devices1:
    print(device)


devices2 = [
    {"hostname": "R1", "status": "Online"},
    {"hostname": "R2", "status": "Offline"},
    {"hostname": "SW1", "status": "Online"}
]

for device in devices2:
    print(device["hostname"])




#Practical Exercise: Multi-Device Inventory Report



devices3 = [
    {
        "hostname": "BR1-R1",
        "ip_address": "192.168.10.1",
        "device_type": "Router",
        "status": "Online"
    },
    
    {
        "hostname": "BR2-SW1",
        "ip_address": "192.168.20.2",
        "device_type": "Switch",
        "status": "Online"
    },
    {
        "hostname": "HQ-FW1",
        "ip_address": "192.168.1.254",
        "device_type": "Firewall",
        "status": "Offline"
    }
]

print("NETWORK DEVICE INVENTORY REPORT")
print("=" * 32)
for device in devices3:
    print(f"Hostname: {device['hostname']}")
    print(f"IP Address: {device['ip_address']}")
    print(f"Device Type: {device['device_type']}")
    print(f"Status: {device['status']}")
    print("=" * 32)

print("Inventory processing completed.")





#Combining for loops with if statements


devices5 = [
    {"hostname": "BR1-R1", "status": "Online"},
    {"hostname": "BR2-SW1", "status": "Online"},
    {"hostname": "HQ-FW1", "status": "Offline"}
]

for device in devices5:
    if device["status"] == "Offline":
        print(f"ALERT: {device['hostname']} is offline!")



devices6 = [
    {"hostname": "HQ-R1", "status": "Online"},
    {"hostname": "BR1-SW1", "status": "Offline"},
    {"hostname": "BR2-R1", "status": "Online"},
    {"hostname": "HQ-FW1", "status": "Offline"},
    {"hostname": "BR3-SW1", "status": "Online"}
]

print("NETWORK DEVICE STATUS CHECK")
print("-" * 32)
for device in devices6:
    if device["status"] == "Offline":
        print(f"Alert: {device['hostname']} is offline")
print("-" * 32)
print("Status check completed.")


#Next challenge: Using if and else together

for device in devices6:
    if device["status"] == "Offline":
        print("OFFLINE")
    else:
        print("ONLINE")