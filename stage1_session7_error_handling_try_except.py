
#ERROR HANDLING
port_number = "443"
port_number = int(port_number)


try:
    response_time = 100 / 0
    print(response_time)

except:
    print("An error occurred")



#EXERCISE 1

try:
    latency = 100 / 0
    print(latency)

except:
    print("Unable to calculate latency")



try:
    latency1 = 100 / 2
    print(latency1)

except:
    print("Unable to calculate latency")

print("Monitoring continues")



#Handling specific exceptions

try:
    port = int("hello")
    print(port)

except ValueError:
    print("Invalid port number")



#using zerodivisionerror


try:
    latency2 = 100 / 0
    print(latency2)

except ZeroDivisionError:
    print("Cannot calculate latency using zero")


#Handling different exceptions in one program

try:
    port = int("hello")
    latency4 = 100 / 0

except ValueError:
    print("Invalid port number")

except ZeroDivisionError:
    print("Cannot divide by zero")




#A practical exercise

try:
    port_number = "hello"
    port_number = int("hello")
    print("Port number:", port_number)

except ValueError:
    print("Invalid port number")




try:
    port_number = "443"
    port_number = int("443")
    print("Port number:", port_number)

except ValueError:
    print("Invalid port number")