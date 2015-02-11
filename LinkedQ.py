class Node:
   def __init__(self, init_data):
      self.data = init_data
      self.next = None
   
   def get_data(self):
      return self.data

   def get_next(self):
      return self.next

   def set_data(self, new_data):
      self.data = newdata

   def set_next(self, new_next):
      self.next = new_next

   def __str__(self):
      return str(self.data)

class LinkedQ:

   def __init__(self):
      self.last = None
      self.first = None

   def enqueue(self, item):
   		
      if self.first == None:
         temp = Node(item)
         self.first = temp
         self.last = temp

      else:
         temp = Node(item)
         self.last.set_next(temp)
         self.last = temp

   def size(self):
      current = self.last
      count = 0
		
      while current != None:
         count = count + 1
         current = current.get_next()
	
      return count

   def is_empty(self):
      return self.first == None

   def dequeue(self):
      first_object = self.first
      self.first = self.first.get_next()
      return first_object
      

def enqueueCards(a_queue, a_list):
     for i in a_list:
          a_queue.enqueue(i)

def sortCards(a_queue):
     the_sorted_cards = []
     while not a_queue.is_empty():
          a_queue.enqueue(a_queue.dequeue())
          first_card = a_queue.dequeue()
          the_sorted_cards.append(first_card)
     return the_sorted_cards


def main():
   q = LinkedQ()
   cards_input = "7 1 12 2 8 3 11 4 9 5 13 6 10"	#input("Write in what order you want the cards, by name or number and seperate by space, eg. 2 3 4 5 or two three four five. :\n")
   card_list = cards_input.split()
   enqueueCards(q, card_list) 
   cards_sorted = sortCards(q)
   for i in cards_sorted:
      print (i, end = " ")

main()





