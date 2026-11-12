network_devices = {
    "BR1-R1": {
        "ip_address": "192.168.10.1",
        "device_type": "Router",
        "status": "Online"
    },
    "BR1-SW1": {
        "ip_address": "192.168.10.2",
        "device_type": "Switch",
        "status": "Online"
    },
    "BR1-SW2": {
        "ip_address": "192.168.10.3",
        "device_type": "Switch",
        "status": "Offline"
    }
}

print(network_devices)

print(network_devices["BR1-R1"]["ip_address"])

network_devices["BR1-AP1"] = {
    "ip_address": "192.168.10.4",
    "device_type": "Access Point",
    "status": "Online"
}

network_devices["BR1-SW2"]["status"] = "Online"

del network_devices["BR1-SW1"]

print(network_devices)
print(len(network_devices))