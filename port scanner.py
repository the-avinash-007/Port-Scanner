# This program has been coded in Visual Studio Code by Avinash Shandilya.

# Creating a port scanner using Python3.
import sys
import socket
from datetime import datetime
#define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate host name to IPV4
else:
    print("Invalid amount of arguments.")
    print("syntax: python3 scanner.py <ip>")

# Adding a banner
print("-" * 50)
print("Scanning Target "+target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # Returns an error indicator 
        if result == 0:
            print("Port {} is open".format(port))
            s.close()

# Some Exceptions

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to the server.")
    sys.exit()