'''
@author: Devangini Patel
'''

class Node:
    '''
    This class represents a node in the search tree
    '''
    
    def __init__(self, state):
        """
        Constructor
        """
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = None
        
        
    def addChild(self, childNode):
        """
        This method adds a node under another node
        """
        self.children.append(childNode)
        childNode.parent = self
        childNode.depth = self.depth + 1
        
    #This method prints the entire tree starting from the current node.
    def printTree(self): 
        """
        This method prints the tree
        """
        #Prints the current node's depth and the person's name 
        print (self.depth , " - " , self.state.name)
        #Iterates over the list of children.
        #Recursively calls printTree on each child node:prints root to leaf node
        for child in self.children:
            child.printTree()
 
    
    def printPath(self):
        """
        This method prints the path from initial state to goal state
        """
        #Checks if the current node has a parent.
        #Recursively calls printPath on the parent node to 
        #trace the path back to the root.
        if self.parent != None:
            self.parent.printPath()
        print ("-> ", self.state.name)