
hostname = "  BR1-R1  "

clean_hostname = hostname.strip()

print(clean_hostname)

#.strip() removes whitespace from the beginning and end of a string.

interface = "  Gi0/1  "
print(interface.strip())

#.split() splits a string into a list of substrings based on whitespace by default.

ip_address = "192.168.1.1"

parts = ip_address.split(".")

print(parts)

#.startswith() checks if a string starts with a specified substring and returns True or False.

hostname = "BR1-R1"

print(hostname.startswith("BR1"))

#.replace() replaces occurrences of a specified substring with another substring.

interface = "GigabitEthernet0/1"

updated_interface = interface.replace("GigabitEthernet", "Gi")

print(updated_interface)


device_info = "  BR2-SW1,192.168.20.10,GigabitEthernet0/1,UP  "

# 1. Remove unnecessary spaces
cleaned_info = device_info.strip()

# 2 & 3. Split using the comma and store in device_details (using cleaned_info)
device_details = cleaned_info.split(",")

# 4. Print the resulting list
print(device_details)

# 5. Check whether the hostname starts with "BR2" (using the first element of the list)
hostname_check = device_details[0].startswith("BR2")
print(hostname_check)

# 6. Replace "GigabitEthernet" with "Gi" in the interface name (index 2)
device_details[2] = device_details[2].replace("GigabitEthernet", "Gi")
print(device_details)


# list of strings
devices = ["BR1-R1", "BR2-SW1", "BR3-R3", "BR4-SW2", "BR5-R5", "BR6-SW3"]
print(devices[0])
print(devices[-1])

devices = ["BR1-R1", "BR1-SW1", "BR2-R1"]

#add an item to the list using.append() and .insert() methods
devices.append("HQ-R1")

print(devices)
devices.insert(1, "BR1-FW1")

print(devices)

#remove an item from the list
devices.remove("BR1-SW1")

print(devices)

#Also remove an item form the list using.pop() method-which uses the index for that
devices.pop(0)

print(devices)

#Finding out how many items are in a list using len() method

devices = ["BR1-R1", "BR1-SW1", "BR2-R1", "HQ-R1"]

print(len(devices))


#Checking whether an item exists using the in operator
devices = ["BR1-R1", "BR1-SW1", "BR2-R1"]

print("BR2-R1" in devices)
print("HQ-R1" in devices)

#Selecting part of a list: slicing list_name[start:end]
devices = ["BR1-R1", "BR1-SW1", "BR2-R1", "BR2-SW1", "HQ-R1"]

print(devices[0:2])


#EXERCISES


devices = ["R1", "SW1", "R2", "SW2"]

print(devices)

devices.append("FW1")
devices.insert(1, "CORE-SW1")

print(devices)

devices.remove("R2")

print(len(devices))

print("FW1" in devices)

print(devices[0:2])



#TUPLES

router = ("R1", "192.168.1.1", "Router", "Lagos")

print(router)

router = ("R1", "192.168.1.1", "Router", "Lagos")

print(router[0])
print(router[1])
print(router[2])
print(router[3])

#Tuples are immutable, meaning you cannot change their values after creation.
#finding the length of a tuple using len() method
router = ("R1", "192.168.1.1", "Router", "Lagos")

print(len(router))


#checking whether an item exists in a tuple using the in operator
router = ("R1", "192.168.1.1", "Router", "Lagos")

print("R1" in router)
print("SW1" in router)


#Counts how many times a value appears using the .count() method
interfaces = ("Gi0/1", "Gi0/2", "Gi0/1", "Gi0/3")

print(interfaces.count("Gi0/1"))

#Returns the index of the first occurrence of a value using the .index() method
interfaces = ("Gi0/1", "Gi0/2", "Gi0/1", "Gi0/3")

print(interfaces.index("Gi0/2"))


#Unpacking a tuple using multiple variables

router = ("R1", "192.168.1.1", "Lagos")
hostname, ip_address, location = router
print(hostname)
print(ip_address)
print(location)

