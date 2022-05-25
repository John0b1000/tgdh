# file: tree_write.py
#

# sources: https://docs.python.org/3/library/pickle.html
#

from Tree import Tree
import sys
import pickle
import socket
import sys

# declare server variables
#
LENGTH = 2048
PORT = 9000
SERVER = sys.argv[1]
ADDR = (SERVER, PORT)

# determine the number of nodes
#
NUM_NODES = int(sys.argv[2])-1

# instantiate the Tree class
#
tree = Tree()

# add the proper number of members
#
for i in range(NUM_NODES):
   tree.insertNewUser()
print("")
print("Generating binary tree with " + sys.argv[2] + " nodes ...\n")
print(tree)

# serialize the tree using the pickle module
#
#serial_data = pickle.dump(tree, open("pickle0.raw", "wb"))
print("\nSerializing tree object and sending to server ...\n")
serial_data = pickle.dumps(tree)
print("Serial object data sent!\n")

# send the message
#
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)
clientSocket.send(serial_data)

"""

# print the pickleMsg for analysis
# this is the message sent to the server (byte stream)
#
serialHex = serial_data.hex()
serialList = [serialHex[i : i + 4] for i in range(0, len(serialHex), 4)]
counter = 0
print("\nPrinting byte stream sent to server ...\n")
for group in serialList:
   if (counter == 0):
      print("0x0000: ", end=" ")
      print(group, end=" ")
      counter = counter + 2
   else:
      if (counter % 16 != 0):
         print(group, end=" ")
         counter = counter + 2
      else:
         print("\n0x%s: " % (hex(counter).lstrip("0x").rjust(4,"0")), end=" ")
         print(group, end=" ")
         counter = counter + 2

print("\n")
# end print
"""
