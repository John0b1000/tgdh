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
import pickle
class Tree(object):
    def __init__(self,maxSize = 30000):
        
        self.root = Node(0,self)
        
        self.array = [self.root] + list([None]*(2*maxSize+10))
        
        self.nodeCount = 1
        self.queue = deque()
        self.queue.append(self.root)

    def left(self,node):
        x =  self.array[2*node.id + 1]
        return x
    def right(self,node):
        x =  self.array[2*node.id + 2]
        return x
    def parent(self,node):
        if(node.id==0):
            x =  node
        else:
            x =  self.array[((node.id)-1)//2]
        return x 
    def setLeft(self,x,target):
        self.array[2*x.id + 1] = target
    def setRight(self,x,target):
        self.array[2*x.id + 2] = target
    def setParent(self,x,target):
        if(x.id==0):
            return 
        self.array[(x.id-1)//2] = target
    def setLeaf(self,x):
        
        self.setLeft(x,None)
        self.setRight(x,None)

        x.isLeaf=True
    def findSponsor(self):
        front = self.queue[0]
        if(front.left() is None and front.right() is None):
            self.queue.popleft()
            return front
        else:
            print("Node deformed")
            return None
    def insertNewUser(self):
        sponsor = self.findSponsor()
        leftNewNode = self.createNode()
        self.queue.append(leftNewNode)
        rightNewNode = self.createNode()
        self.queue.append(rightNewNode)
        leftNewNode.setParent(sponsor)
        rightNewNode.setParent(sponsor)
        leftNewNode.copyDataFrom(sponsor)
        sponsor.isLeaf = False
        
        sponsor.setLeft(leftNewNode)
        sponsor.setRight(rightNewNode)
        sponsor.recalculateKeyPath()
    def deleteNewUser(self):
        toDelete = self.queue[-1]
        
        if(toDelete.parent().left().id==toDelete.id):
            toDelete.parent().copyDataFrom(toDelete.parent().right())
        
        else:
            toDelete.parent().copyDataFrom(toDelete.parent().left())
        self.setLeaf(toDelete.parent())
        toDelete.parent().recalculateKeyPath()
        
        self.queue.pop()
        self.queue.pop()
        self.queue.appendleft(toDelete.parent())
        
    def removeUser(self,id):
        pass
    
    def createNode(self):
        newNode = Node(self.nodeCount,self)
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


NUM_NODES=10000 
tree = Tree()
y = []
x = []
for i in range(NUM_NODES):
    start = time.time()
    tree.insertNewUser()
    end = time.time()
    if(i%50==0):
        print(i)
        y.append(end - start)
        x.append(i)
# print(tree.verifyTreeIntegrity())
data=[x,y]
file=open("insertion_time","wb")
pickle.dump(data,file)
file.close()
plt.plot(x,y,"o-")
plt.xlabel("Number of users")
plt.ylabel("Time for insertion(sec)")
plt.savefig("./insertion_time_plot.png")
plt.clf()
x=[]
y=[]
for i in range(NUM_NODES):
    start = time.time()
    tree.deleteNewUser()
    end = time.time()
    if(i%50==0):
        print(i)
        y.append(end - start)
        x.append(NUM_NODES-(i+1))
    
# print(tree.verifyTreeIntegrity())
data=[x,y]
file=open("deletion_time","wb")
pickle.dump(data,file)
file.close()
plt.plot(x,y,"o-")
plt.xlabel("Number of users")
plt.ylabel("Time for deletion(sec)")
plt.savefig("./deletion_time_plot.png")
plt.show()

