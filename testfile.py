#Test enqueue method
def test_enqueue():
q = ListQ
q.enqueue(1)
if q[0] == 1
	print("funktionen fungerar.")
else:
	print("Funktionen fungerar inte.")


def test_dequeue():
#Test dequeue method
q = ListQ
q.enqueue(5)	
if q.dequeue() == 5:
	print("funktionen fungerar.")

else:
	print("Funktionen fungerar inte.")


def test_size():
#Test size method
q = ListQ
q.enqueue(1)
if q.size() == 1
	print ("funktionen fungerar.")
else:
	print("funktionen fungerar inte")


def test_enqueCards():
#test enqueueCards
q = ListQ
test_list = [4,5,6]

enqueueCards(q, test_list)

if q.self.items == ("4, 5, 6"):
	print("Koden fungerar")
else:
	print("koden fungerar inte")


def sortCards(q):
	the_sorted_cards = []
	while not q.is_empty():
		q.enqueue(q.dequeue())
		card_to_show = q.dequeue()
		the_sorted_cards.append(card_to_show)	
	return the_sorted_cards


def test_sortCards():
	q = [7,1,12,2,8,3,11,4,9,5,13,6,10]

	if sortCards(q) == [1,2,3,4,5,6,7,8,9,10,11,12,13]:
 		print("Funktionen fungerar")

	else:
 		print("Funktionen fungerar ej")




