
device = {
    "hostname": "BR1-SW1",
    "ip_address": "192.168.10.2",
    "device_type": "Switch",
    "location": "Branch 1",
    "status": "Online"
}
print(device["hostname"])
print(device["ip_address"])

#TO PRINT BOTH KEY AND VALUE USING F STRING

print(f"hostname: {device['hostname']}")
print(f"ip_address: {device['ip_address']}")

#ADDING A NEW KEY-VALUE PAIR TO THE DICTIONARY
device["port_count"] = 24
print(device)

#UPDATE AN EXISTING KEY-VALUE PAIR IN THE DICTIONARY
device["ip_address"] = "192.168.10.5"
print(device)


#UPDATE MULTIPLE KEY-VALUE PAIRS IN THE DICTIONARY
device.update({
    "status": "Offline",
    "location": "Main Office"
})
print(device)


##REMOVE A KEY-VALUE PAIR FROM THE DICTIONARY USING DEL
del device["port_count"]
del device["location"]
print(device)

#METHOD 2 FOR REMOVING DICTIONARY USING .POP() METHOD
device.pop("status")

#YOU CAN ALSO PROVIDE A DEFAULT VALUE TO RETURN IF THE KEY DOES NOT EXIST

device.pop("serial_number", "Not found")
print(device)

#METHOD 3 FOR REMOVING A KEY-VALUE PAIR FROM THE DICTIONARY USING .CLEAR() METHOD

#device.clear()

#CHECKING IF A KEY EXISTS IN THE DICTIONARY USING IF METHOD

if "ip_address" in device:
    print("IP address exists in the dictionary.")


#TO CHECK WHETHER A KEY DOES NOT EXIST IN THE DICTIONARY USING NOT IN METHOD

if "serial_number" not in device:
    print("Serial number is missing")

print(device.keys())

print(device.values())

#You can also loop through a dictionary

for key, value in device.items():
    print(key, value)