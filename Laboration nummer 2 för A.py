from ListQclass import ListQ
from LinkedQclass import LinkedQ
from StackClass import Stack

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



def main():
   q = ListQ()
   cards_input = input("\nPlease input cards from 1-13 in increasing size and seperate them by space. Either by name or number, eg 1 2 3 4 or ace two three four:\n")
   card_list = cards_input.split()
   cards_stacked = stackCards(card_list)
   enqueueCards(q, cards_stacked)
   cards_sorted = sortCards(q)
   cards_sorted = revertOrder(cards_sorted)
   print("\n\n\n")
   for i in cards_sorted:
      print (i, end = " ")
   print("\nYour cards have now been re-ordered so that you can use that particular order to do a magic trick.")

main()





