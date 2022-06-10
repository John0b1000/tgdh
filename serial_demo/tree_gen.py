# file: tree_gen.py
#

from Tree import Tree
import sys

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
    
# print the tree
#
print("")
print("Generating binary tree with " + sys.argv[2] + " nodes ...\n")
print(tree)
