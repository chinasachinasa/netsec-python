failed_login_ips = [
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.15",
    "192.168.1.25",
    "192.168.1.10",
    "192.168.1.30"
]

# 1. Convert the list into a set
unique_ips = set(failed_login_ips)

# 2. Print the set
print(unique_ips)

# 3. Print the number of unique IP addresses
print(len(unique_ips))



branch_1 = {"R1", "R2", "SW1", "SW2"}
branch_2 = {"R2", "R3", "SW2", "SW3"}

# 1. All devices across both branches (Union)
all_devices = branch_1.union(branch_2)          # or: branch_1 | branch_2
print("All devices:", all_devices)

# 2. Devices common to both branches (Intersection)
common_devices = branch_1.intersection(branch_2) # or: branch_1 & branch_2
print("Common devices:", common_devices)

# 3. Devices only in Branch 1 (Difference)
only_branch_1 = branch_1.difference(branch_2)    # or: branch_1 - branch_2
print("Only in Branch 1:", only_branch_1)

# 4. Devices only in Branch 2 (Difference)
only_branch_2 = branch_2.difference(branch_1)    # or: branch_2 - branch_1
print("Only in Branch 2:", only_branch_2)



devices = {"R1", "R2", "SW1"}

# 1. Add R3
devices.add("R3")

# 2. Remove R2
devices.remove("R2")

# 3. Attempt to discard SW5 (does not raise an error if missing)
devices.discard("SW5")

# 4. Print the final set
print(devices)