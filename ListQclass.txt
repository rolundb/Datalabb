class ListQ:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, an_item):
		self.items.insert(0, an_item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def __str__(self):
		return str(self.items)
