#try:
 #   file = open("network_inventory.txt", "r")
#except FileNotFoundError:
 #   print("Network inventory file not found.")

#except OSError:
#    print("An operating system error occurred.")


#The with open() approach handles this automatically. When Python finishes reading the file, it closes it, even if an exception occurs.
#This is why we generally prefer:

#with open("network_inventory.txt", "r") as file:
    #content = file.read()


#Practical file handling: try, except and with open()
try:
    with open("switch_inventory.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("ERROR: Switch inventory file not found.")



#Next: Practical OSError handling

try:
    with open("network_inventory.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("ERROR: Network inventory file not found.")

except PermissionError:
    print("ERROR: You do not have permission to access this file.")

except OSError:
    print("ERROR: An operating system error occurred.")

finally:
    print("Network inventory operation completed.")



#Practical exercise 7: Network inventory troubleshooting
#Scenario: You are a junior NOC technician. Your Python script reads a text file containing the IP addresses of routers and switches that the team monitors.

try:
    with open("network_inventory.txt", "r") as inventory_file:
        content = inventory_file.read()
        print(content)
except FileNotFoundError:
    print("ERROR: Network inventory file not found.")
except OSError:
    print("ERROR: Unable to access the network inventory.")
finally:
    print("NOC inventory check completed.")



#python can also creates and write files

with open("network_report.txt", "w") as file:
    file.write("Router1: Operational")
    file.write("Router2: Operational")
    file.write("Router3: Offline")
    file.write("Router1: in use")