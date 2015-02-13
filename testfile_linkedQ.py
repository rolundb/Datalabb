from ListQclass import ListQ
from LinkedQclass import LinkedQ
from StackClass import Stack
from LinkedQclass import Node

# Puts all elements of a stack in a queue.
#
# parameter1 a_queue      A queue.
# parameter2 a_list       A list.
# return: None
def enqueueCards(a_queue, a_stack):
     while not a_stack.is_empty():
      a_queue.enqueue(a_stack.pop())


# Takes a queue of elements and puts them in the order meant for the
# magic trick to be succesfull.
#
# parameter1 a_queue      A queue.
# return: the_sorted_cards    A list of the elements in right order for the magic trick.
def sortCards(a_queue):
     the_sorted_cards = []
     while not a_queue.is_empty():
          the_sorted_cards.append(a_queue.dequeue())
          the_sorted_cards.append(the_sorted_cards.pop(0))
     return the_sorted_cards


# Takes a list of elements and puts them in a stack
#
# parameter1 a_list      A list.
# return: the_stack   The stack created from the list used as parameter1.
def stackCards(a_list):
  the_stack = Stack()
  for i in a_list:
    the_stack.push(i)
  return the_stack



# Reverts the order of a list by using a stack.
#
# parameter1 a_list      A list.
# return: the_reverted_cards    A list same as parameter1 but elements in inverted order. 
def revertOrder(a_list):
  the_stack = Stack()
  the_reverted_cards = []
  for i in a_list:
    the_stack.push(i)
  while not the_stack.is_empty():
    the_reverted_cards.append(the_stack.pop())
  return the_reverted_cards



########################TESTS BELOW########################

def test_get_data():
	indata = 1
	node1 = Node(indata)

	if node1.get_data == indata:
		print("funktionen fungerar.")
	else:
		print("Funktionen fungerar inte.")


def test_get_next():

  indata = 1
  node1 = Node(indata)

  if node1.get_next() == None:
  	print("funktionen fungerar.")
  else:
  	print("funktionen fungerar ej")


def test_set_data():

  test_init = 1
  test_node = Node(test_init)
  newdata = 2

  test_node.set_data(newdata)

  if test_node.data == newdata:
  	print("Funktoinen fungerar")
  else:
  	print("Funktionen fungerar inte")


def test_set_next():

  test_init = 1
  test_node = Node(test_init)
  new_next = 2

  test_node.set_next(new_next)

  if test_node.next == new_next:
  	print("Funktoinen fungerar.")
  else:
  	print("Funktionen fungerar inte.")

def test_stackCards():
  a_list = [1,2,3]
  if stackCards(a_list) == [1,2,3]:
    print("Funktionen fungerar.")
  else:
    print("Funktionen fungerar inte.")



def test_revertOrder():
  a_list = [1,2,3]

  if revertOrder(a_list) == [3,2,1]:
    print("Funktionen fungerar")
  else:
    print("Funktionen fungerar inte")
  


test_get_data()
test_set_next()
test_set_data()
test_get_next()
test_stackCards()
test_revertOrder()



