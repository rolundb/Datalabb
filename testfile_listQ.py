#7 1 12 2 8 3 11 4 9 5 13 6 10

from ListQclass import ListQ
from LinkedQclass import LinkedQ


# Takes all elements in a list and puts them in a queue.
#
# parameter1 a_queue      A queue.
# parameter2 a_list       A list of elements.
# return: None
def enqueueCards(a_queue, a_list):
     for i in a_list:
          a_queue.enqueue(i)


# Takes a queue of elements and puts them in the order meant for the
# magic trick to be succesfull.
#
# parameter1 a_queue      A queue of elements.
# return: the_sorted_cards    A list of elements in the right order for ther magic trick to be succesfull.
def sortCards(a_queue):
     the_sorted_cards = []
     while not a_queue.is_empty():
          a_queue.enqueue(a_queue.dequeue())
          first_card = a_queue.dequeue()
          the_sorted_cards.append(first_card)
     return the_sorted_cards



def main():
   q = ListQ()
   cards_input = input("Please write the cards in the order given to you by program1, by name or number and seperate by space, eg. 2 3 4 5 or two three four five. :\n")
   card_list = cards_input.split()
   enqueueCards(q, card_list) 
   cards_sorted = sortCards(q)
   for i in cards_sorted:
      print (i, end = " ")



########################TESTS BELOW#########################




#Test enqueue method
def test_enqueue():
	q = ListQ()
	q.enqueue(1)
	if q.items[0] == 1:
		print("funktionen fungerar.")
	else:
		print("Funktionen fungerar inte.")

def negative_test_enqueue():
	q = ListQ()
	q.enqueue(1)
	if q.items[0] == 2:
		print("Negativt test fungerar inte.")
	else:
		print("Negativt test fungerar.")

def test_dequeue():
	#Test dequeue method
	q = ListQ()
	q.enqueue(5)	
	if q.dequeue() == 5:
		print("funktionen fungerar.")
	else:
		print("Funktionen fungerar inte.")

def negative_test_dequeue():
	q = ListQ()
	try:
		q.dequeue()
		print("Negativt test fungerar inte.")
	except:
		print("Negativt test fungerar.")


def test_size():
	#Test size method
	q = ListQ()
	q.enqueue(1)
	if q.size() == 1:
		print ("funktionen fungerar.")
	else:
		print("funktionen fungerar inte")


def test_enqueCards():
	#test enqueueCards
	q = ListQ()
	test_list = [4,5,6]

	enqueueCards(q, test_list)

	if q.items == [6, 5, 4]:
		print("Funktionen fungerar")
	else:
		print("Funktionen fungerar inte")

def test_sortCards():
	q = ListQ()
	q.items = [10,6,13,5,9,4,11,3,8,2,12,1,7]

	if sortCards(q) == [1,2,3,4,5,6,7,8,9,10,11,12,13]:
 		print("Funktionen fungerar")

	else:
 		print("Funktionen fungerar ej")


test_size()
test_dequeue()
test_enqueue()
test_sortCards()
test_enqueCards()
negative_test_enqueue()
negative_test_dequeue()
