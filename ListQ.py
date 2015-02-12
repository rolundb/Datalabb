def enqueueCards(a_queue, a_list):
	for i in a_list:
		a_queue.enqueue(i)

def sortCards(q):
	the_sorted_cards = []
	while not q.is_empty():
		q.enqueue(q.dequeue())
		card_to_show = q.dequeue()
		the_sorted_cards.append(card_to_show)
	return the_sorted_cards


def main():
	q = ListQ()
	cards_input = "7 1 12 2 8 3 11 4 9 5 13 6 10"	#input("Write in what order you want the cards, by name or number and seperate by space, eg. 2 3 4 5 or two three four five. :\n")
	card_list = cards_input.split()
	enqueueCards(q, card_list) 
	cards_sorted = sortCards(q)
	for i in cards_sorted:
		print (i, end = " ")

main()







