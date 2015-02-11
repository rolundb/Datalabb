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
        
def cardTrick(a_card_list):
    the_table_cards = ListQ() 
    for card in str(a_card_list):
        i = 0
        if i%2 == 0:
            the_table_cards.put(card)
        else:
            a_card_list.put(a_card_list.get())

    print(the_table_cards)

kort = ListQ()  
for i in range(13):
    kort.put(i)

print(kort)



