
import os
from getpass import getpass
from netmiko import ConnectHandler

# Read connection details from environment variables
host = os.getenv("NETMIKO_HOST")
username = os.getenv("NETMIKO_USERNAME")

# Check that the required variables exist
if not host or not username:
    raise SystemExit("Missing router connection details.")

# Request password securely
password = getpass("Enter router password: ")

# Define the router
device = {
    "device_type": "cisco_xe",
    "host": host,
    "username": username,
    "password": password,
    "port": 22,
}

# Establish SSH connection
connection = ConnectHandler(**device)

try:
    print("\nConnected successfully!")
    print("\nRetrieving router information...\n")

    output = connection.send_command("show version")
    print(output)

finally:
    connection.disconnect()
    print("\nSSH connection closed.")
