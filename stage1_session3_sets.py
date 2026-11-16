#SETS

failed_logins = [
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.10",
    "192.168.1.20"
]

unique_ips = set(failed_logins)

print(unique_ips)



#creating sets
#Method 1: Using curly braces

devices = {"R1", "R2", "SW1", "SW2"}

print(devices)


#Method 2: Using the set() function

devices = set(["R1", "R2", "SW1", "SW2"])

print(devices)



#Adding an element

devices = {"R1", "R2", "SW1"}

devices.add("R3")

print(devices)

#Removing an element
devices.remove("R2")
print(devices)

devices.discard("R2")
print(devices)


##Set Operations - union, intersection, difference

branch_1 = {"R1", "R2", "SW1"}
branch_2 = {"R3", "SW1", "FW1"}

all_devices = branch_1.union(branch_2)
print(all_devices)
# Output: {'R1', 'R2', 'SW1', 'R3', 'FW1'} (notice "SW1" is not duplicated)


#B. Intersection: Find common devices

common_devices = branch_1.intersection(branch_2)

print(common_devices)

#C. Difference: Find devices in one set but not the other

unique_branch_1 = branch_1.difference(branch_2)

print(unique_branch_1)