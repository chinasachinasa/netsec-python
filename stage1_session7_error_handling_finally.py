
try:
    print("Checking network device")

except:
    print("An error occurred")

finally:
    print("Monitoring process completed")


#What happens when an exception occurs?

try:
    response_time = 100 / 0
    print(response_time)

except ZeroDivisionError:
    print("Unable to calculate response time")

finally:
    print("Monitoring process completed")



#EXERCISE

try:
    port = int("443")
    print("Port:", port)

except ValueError:
    print("Invalid port number")

finally:
    print("Port validation completed")




#Next exercise: Let's test what happens when an error occurs

try:
    port = int("hello")
    print("Port:", port)

except ValueError:
    print("Invalid port number")

finally:
    print("Port validation completed")




#EXERCISE

try:
    port_number = int("hello")
    print("Valid port:", port_number)

except ValueError:
    print("Invalid port number")

finally:
    print("Port validation completed")