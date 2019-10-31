# Import socket module 
import socket                
from client_utils import *

class Client:
    choice = None

    def __init__(self, choice):
        self.choice = choice
    
    def get_data(self):
        # Create a socket object 
        s = socket.socket()          
        
        # Define the port on which you want to connect 
        port = 65432                
        
        # connect to the server on local computer 
        s.connect(('127.0.0.1', port))

        # Receive input
        turn = self.choice

        # Send input
        s.send(turn.encode('utf-8'))

        # receive data from the server 
        statement = s.recv(1024).decode('utf-8')
        # close the connection 
        s.close()
        return statement
        



