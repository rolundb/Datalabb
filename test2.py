<<<<<<< Updated upstream

class ListQ:

def __init__(self):
    self.the_list = []

def __str__(self):
    return str(self.the_list)

def put(self, item):
    self.the_list.append(item)

def get(self):
    return self.the_list.pop()

def isEmpty(self):
    return self.the_list == []

def size(self):
    return len(self.the_list)


#Test 1
q = ListQ()

if q.isEmpty():
    print("q.isEmpty() ger rätt svar.")

else:
    print("q.isEmpty() ger FEL svar.")





def cardTrick(a_card_list, a_number):
    #Skapar en kö
    card_deck = ListQ()
    table_cards = ListQ()
    for card in a_card_list:
            card_deck.put(card)


    for card in a_card_list:
            i = 0
            for i in range(a_number):
                    if i % 2  == 0:
                            table_cards.put(card)
                    else:
                            card_deck.put(card)


    while card_deck.size() > 1:
antalkort = 13
kort = [1,2,3]
cardTrick(kort, antalkort)






=======
q = Queue()

q.enqueue("hej")

print(q)
>>>>>>> Stashed changes
