# file: tree_read.py
#

from Node import Node
from Tree import Tree
import socket
import threading
import pickle

# declare server variables
#
LENGTH = 1000000
PORT = 9000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# create a server so that data can be transmitted
#
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(ADDR)
serverSocket.listen()
print("")
print(f"Server is listening on {SERVER}")

def getTree(connection, addr):
    print(f"New connection - {addr}")
    connected = True
    while connected:
        tree = pickle.loads(connection.recv(LENGTH))
        print("\nBinary tree received!\n")
        print(tree)
        connected = False
    connection.close()
    print(f"Connection closed - {addr}")
    div = "-"
    print("")
    print(div.ljust(80,"-"))
    print("")

while True:
  connection, addr = serverSocket.accept()
  thread = threading.Thread(target=getTree, args=(connection, addr))
  thread.start()
  print(f"Number of connections: {threading.activeCount() - 1}")
