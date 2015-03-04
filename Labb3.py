import re
from random import shuffle
import time


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


def uppgift2():
  svenska = Bintree()
  with open("word3.txt", "r", encoding = "utf-8") as swefile:
      for row in swefile:
          word = row.strip()                
          if svenska.exists(word):
              print(word, end = " ") 
          else:
              svenska.put(word)            
  print("\n")

def uppgift3():
  svenska = Bintree()
  with open("word3.txt", "r", encoding = "utf-8") as swefile:
      for row in swefile:
          word = row.strip()               
          if svenska.exists(word) == False:
              svenska.put(word)             
  
  engelska = Bintree()
  with open("engelska.txt", "r", encoding = "utf-8") as engfile:
    for row in engfile:
      for word in row.split():
        word = re.sub("[^A-Za-z]", "", word)
        if engelska.exists(word) == False and svenska.exists(word) == True:
          print(word, end= " ")
          engelska.put(word)

def uppgift4():

#Stores a value in the tree. If there is a root object,
#tests if the value is already in the tree. If it is not
#then adds a new child to the root.
#
# return: number_list   A list of shuffled numbers.
  def randomList():
    number_list = [i for i in range(10000000000000000000000000000000000000000000000000)]
    shuffle(number_list)
    return number_list

#Fills a tree with objects from list.
#
# parameter1 tree      A tree.
# parameter2 list  A list with objects.
# return: None
  def listToTree(tree, list):
    for i in list:
      tree.put(i)

  tree = Bintree()
  random_list = randomList()
  listToTree(tree, random_list)
  tic = time.time()
  value = 35
  if tree.exists(value):
    toc = time.time()
  else:
    print("not found")
  print("Time for tree passed:" + str(toc-tic) + " sec.")
  tic = time.time()
  if value in random_list:
    toc = time.time()
  print("Time for list passed:" + str(toc-tic) + " sec.")


def uppgift5():
  tree = Bintree()
  with open("word3.txt", "r", encoding = "utf-8") as swefile:
      for row in swefile:
          word = row.strip()   
          invert_word = word[::-1]           
          if tree.exists(word) == False:
              tree.put(word)
          if word != invert_word and tree.exists(invert_word) == True:
            print(word + "     " + invert_word)         







