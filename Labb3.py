class Bintree:
  def __init__(self):
      self.root=None

  def put(self,newvalue):
      self.root=putFunc(self.root,newvalue)

  def exists(self,value):
      return existsFunc(self.root,value)

  def write(self):
      writeFunc(self.root)
      print("\n")

  def putFunc(self, root, newValue):
      #Stores a value in the tree. If there is a root object,
      #tests if the value is already in the tree. If it is not
      #then adds a new child to the root
      if root == None:
          return Node(newValue)
      if self.exists(newValue) == False:
          root.newChild(newValue)
      return root

  def existsFunc(self, root, value):
      #Tests if a value already exists in the tree (if there is a root object)
      if root == None:
          return False
      else:
          return root.valueExists(value)

  def writeFunc(self, root):
      #If there is a root, prints out the root and its children
      if root != None:
          root.write()
          print("\n")

class Node:
  
  def __init__(self, value):
      #Init function
      self.value = value
      self.leftChild = None
      self.rightChild = None

  def __str__(self):
      #Returns the value stored in the node
      return(str(self.value))

  def newChild(self, newValue):
      #Adds a new child to the node. If the node already has a child
      #occupying the correct slot, calls newChild on that node instead
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

  def valueExists(self, value):
      #If this nodes value matches the input value, returns true
      #otherwise, if node has a child occupying the correct slot
      #calls a check on the child. If no child exists, returns false
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
          
  def write(self):
      #Prints out the nodes value and the values of the children if they exist
      #Then tells the children to print as well
      print(str(self.value) + " has left child " + str(self.leftChild) + " and right child " + str(self.rightChild))
      if self.leftChild != None:
          self.leftChild.write()
      if self.rightChild != None:
          self.rightChild.write()







