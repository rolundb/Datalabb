class Bintree(object):
    def __init__(self):
        self.root = None


# Adds a value to the tree
#
# parameter1 newValue      Value to be added to the tree.
# return: None
    def put(self, newValue):
        self.root = self.putFunc(self.root, newValue)

# Tests if a value already exists in the tree
#
# parameter1 value      Value to be tested to the tree.
# return: None
    def exists(self, value):
        return self.existsFunc(self.root, value)

# Prints out all nodes in the tree
#
# return: None
    def write(self):
        self.writeFunc(self.root)

#Stores a value in the tree. If there is a root object,
#tests if the value is already in the tree. If it is not
#then adds a new child to the root
#
# parameter1 root      Root of the tree.
# parameter2 newValue  Value to be added to the tree.
# return: root
    def putFunc(self, root, newValue):
        if root == None:
            return Node(newValue)
        if self.exists(newValue) == False:
            root.newChild(newValue)
        return root

#Tests if a value already exists in the tree (if there is a root object)
#
# parameter1 root      Root of the tree.
# parameter2 value     Value to be tested to the tree.
# return: True or False
    def existsFunc(self, root, value):
        if root == None:
            return False
        else:
            return root.valueExists(value)

#If there is a root, prints out the root and its children
#
# parameter1 root      Root of the tree.
# return: None
    def writeFunc(self, root):
        if root != None:
            root.write()
            print("\n")
        

class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return(str(self.value))

#Adds a new child to the node. If the node already has a child
#occupying the correct slot, calls newChild on that node instead
#
# parameter1 newValue  Value for child.
    def newChild(self, newValue):
        
        if newValue < self.value:
            if self.leftChild == None:
                self.leftChild = Node(newValue)
            else:
                self.leftChild.newChild(newValue)
        else:
            if self.rightChild == None:
                self.rightChild = Node(newValue)
            else:
                self.rightChild.newChild(newValue)

#If this nodes value matches the input value, returns true
#otherwise, if node has a child occupying the correct slot
#calls a check on the child. If no child exists, returns false
#
# parameter1 value     Value to be matched against tree.
# return: True or False
    def valueExists(self, value):
        
        if value == self.value:
            return True
        elif value < self.value:
            if self.leftChild == None:
                return False
            else:
                return self.leftChild.valueExists(value)
        else:
            if self.rightChild == None:
                return False
            else:
                return self.rightChild.valueExists(value)

#Prints out the nodes value and the values of the children if they exist
#Then tells the children to print as well
#
# return: None
    def write(self):
        
        print(str(self.value) + " has left child " + str(self.leftChild) + " and right child " + str(self.rightChild))
        if self.leftChild != None:
            self.leftChild.write()
        if self.rightChild != None:
            self.rightChild.write()