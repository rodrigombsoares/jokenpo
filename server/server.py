import socket
from server_utils import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

a=True

while a==True:
    c, addr = sock.accept()      
    print('Got connection from', addr)

    # generate pc hand
    pc_hand = rand_hand()

    # receive turn
    player_hand = c.recv(1024).decode('utf-8')

    # get winner
    winner = get_winner(player_hand, pc_hand)

    # send a thank you message to the client.  
    c.send(('You said '+player_hand+'\nI said '+pc_hand+'\n'+winner).encode('utf-8'))

    # Close the connection with the client 
    c.close()

    a = False