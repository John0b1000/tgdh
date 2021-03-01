"""
class tree
each leaf node would have copy of the tree
each copy has different public and private vars
tree functions :
add node              ]
delete node           ] - Basic functions

merge subtree
remove subtree
assign groups


"""
from Node import Node
import time
from collections import deque
import matplotlib.pyplot as plt
class Tree(object):
    def __init__(self):
        
        self.root = Node(0)
        self.nodeCount = 1
        self.queue = deque()
        self.queue.append(self.root)
    def findSponsor(self):
        front = self.queue[0]
        if(front.left is None and front.right is None):
            self.queue.popleft()
            return front
        else:
            print("Node deformed")
    def insertNewUser(self):
        sponsor = self.findSponsor()
        leftNewNode = self.createNode()
        self.queue.append(leftNewNode)
        rightNewNode = self.createNode()
        self.queue.append(rightNewNode)
        leftNewNode.parent = sponsor
        rightNewNode.parent = sponsor
        leftNewNode.copyDataFrom(sponsor)
        sponsor.isLeaf = False
        
        sponsor.left = leftNewNode
        sponsor.right = rightNewNode
        sponsor.recalculateKeyPath()
    def removeUser(self):
        pass
    
    def createNode(self):
        newNode = Node(self.nodeCount)
        self.nodeCount+=1
        return newNode
    
    def verifyTreeIntegrity(self):
        return self.root.verifyIntegrity()
    def __str__(self):
        output =""
        lines, *_ = self.root.recursivePrint()
        for line in lines:
            output+=line
            output+='\n'
        return output


NUM_NODES=1000 
tree = Tree()
y = []
for i in range(NUM_NODES):
    start = time.time()
    tree.insertNewUser()
    end = time.time()
    y.append(end - start)
x= list(range(NUM_NODES))

plt.plot(x,y,"o-")
plt.xlabel("Number of users")
plt.ylabel("Time for insertion(sec)")
plt.savefig("./insertion_time_plot.png")
plt.show()
# print(tree.verifyTreeIntegrity())
