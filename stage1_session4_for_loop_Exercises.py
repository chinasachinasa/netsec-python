network_devices = [
    {"hostname": "HQ-R1", "status": "Online"},
    {"hostname": "BR1-SW1", "status": "Offline"},
    {"hostname": "BR2-R1", "status": "Online"},
    {"hostname": "HQ-FW1", "status": "Offline"},
    {"hostname": "BR3-SW1", "status": "Online"}
]

print("NETWORK DEVICE MONITORING REPORT")
print("=" * 32)
for device in network_devices:
    if device["status"] == "Online":
        print(f"{device['hostname']}: ONLINE")
    else:
        print(f"{device['hostname']}: OFFLINE")
print("=" * 32)
print("Monitoring completed")



#4. Next concept: Counting online and offline devices

online_count = 0

online_count += 1
online_count += 1
online_count += 1

print(online_count)

network_devices = [
    {"hostname": "HQ-R1", "status": "Online"},
    {"hostname": "BR1-SW1", "status": "Offline"},
    {"hostname": "BR2-R1", "status": "Online"},
    {"hostname": "HQ-FW1", "status": "Offline"},
    {"hostname": "BR3-SW1", "status": "Online"}
]
online_count=0
offline_count=0
for device in network_devices:
    if device["status"] == "Online":
        online_count += 1
    else:
        offline_count += 1
total_devices = online_count + offline_count
print("NETWORK MONITORING SUMMARY")
print(f"Online devices: {online_count}")
print(f"Offline devices: {offline_count}")
print(f"Total devices: {total_devices}")