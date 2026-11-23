
#functions
def check_network():
    print("Checking network connectivity...")
check_network()  


#EXEERCISE 1
def monitor_device():
    print("Monitoring BR1-R1")


monitor_device()
monitor_device()
monitor_device()


#Your practical exercise
def check_connectivity():
    print("Checking network connectivity...")
    print("Network connection is active.")

check_connectivity()
check_connectivity()


#EXERCISE 3

def monitor_device(device_name):
    print(f"Monitoring device: {device_name}")

monitor_device("CORE-R1")


#Reusing the function with different devices

def monitor_device(device_name):
    print("Monitoring device:", device_name)


monitor_device("CORE-R1")
monitor_device("BRANCH-R1")
monitor_device("BRANCH-SW1")



#EXERCISE 4 PARAMETERS AND ARGUMENTS
def check_device_status(device_name):
    print(f"Checking status of {device_name}")


check_device_status("CORE-SW1")
check_device_status("BRANCH-R1")
check_device_status("FIREWALL-1")


#DEFAULT ARGUMENTS

def monitor_device(device_name, interval=5):
    print(f"Monitoring {device_name}")
    print(f"Check interval: {interval} seconds")

#monitor_device("CORE-R1",10)-IT OVER WRITES THE INITIAL 5 SECONDS INTERVAL AND USE THE CURRENT ONE IN THE ARGUMENTS

monitor_device("CORE-R1")


#RETURN VALUE

def count_devices(online_devices, offline_devices):
    total = online_devices + offline_devices
    return total
device_total = count_devices(8, 2)

print(device_total)


#exercise 5

def calculate_network_devices(online_devices, offline_devices):
    total = online_devices + offline_devices
    return total


total_devices = calculate_network_devices(8, 3)
print(f"Total network devices: {total_devices}")