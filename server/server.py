import socket
import threading
from server_utils import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
MAX_CLIENTS = 100    # Max number of simultaneous clients

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(MAX_CLIENTS)

clients    = [None] * MAX_CLIENTS
addr       = [None] * MAX_CLIENTS
cur_client = 0

def handle_game(client_sock):
    # generate pc hand
    pc_hand = rand_hand()

    # receive turn
    player_hand = client_sock.recv(1024).decode('utf-8')

    # get winner
    winner = get_winner(player_hand, pc_hand)

    # send a thank you message to the client.  
    client_sock.send(('You said '+player_hand+'\nI said '+pc_hand+'\n'+winner).encode('utf-8'))
    

while True:
    if(cur_client>=MAX_CLIENTS):
        break
    clients[cur_client], addr[cur_client] = sock.accept()      
    print('Got connection from', addr[cur_client])
    
    game_thread = threading.Thread(target=handle_game, args=(clients[cur_client], ),daemon=True)
    game_thread.start()
    
