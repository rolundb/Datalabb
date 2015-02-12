#7 1 12 2 8 3 11 4 9 5 13 6 10

from ListQclass import ListQ
from LinkedQclass import LinkedQ
from StackClass import Stack

def enqueueCards(a_queue, a_stack):
     while not a_stack.is_empty():
      a_queue.enqueue(a_stack.pop())

def sortCards(a_queue):
     the_sorted_cards = []
     while not a_queue.is_empty():
          the_sorted_cards.append(a_queue.dequeue())
          the_sorted_cards.append(the_sorted_cards.pop(0))
     return the_sorted_cards

def stackCards(a_list):
  the_stack = Stack()
  for i in a_list:
    the_stack.push(i)
  return the_stack


def main():
   q = ListQ()
   cards_input = "1 2 3 4 5 6 7 8 9 10 11 12 13"	#input("Write in what order you want the cards, by name or number and seperate by space, eg. 2 3 4 5 or two three four five. :\n")
   card_list = cards_input.split()
   cards_stacked = stackCards(card_list)
   enqueueCards(q, cards_stacked)
   cards_sorted = sortCards(q)
   for i in cards_sorted:
      print (i, end = " ")

main()





