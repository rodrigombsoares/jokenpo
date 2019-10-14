# Import socket module 
import socket                
from client_utils import *


# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 65432                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port))

# Receive input
turn = get_input()

# Send input
s.send(turn.encode('utf-8'))

# receive data from the server 
print(s.recv(1024).decode('utf-8'))
# close the connection 
s.close()



