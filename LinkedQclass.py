class Node:
   def __init__(self, init_data):
      self.data = init_data
      self.next = None
   
   def get_data(self):
      return self.data

   def get_next(self):
      return self.next

   def set_data(self, new_data):
      self.data = new_data

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
