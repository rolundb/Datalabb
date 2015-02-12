def test_get_data():
	class Node:
		def __init__(self, init_data):
      		self.data = init_data
      		self.next = None

	indata = 1
	node1 = Node(indata)

	if node1.test_get_data == indata:
		print("funktionen fungerar.")
	else:
		print("Funktionen fungerar inte.")


def test_get_next():

	class Node:
		def __init__(self, init_data):
      		self.data = init_data
      		self.next = None

    indata = 1
    node1 = Node(indata)

    if node1.get_next() == None:
    	print("funktionen fungerar för Head-nod")
    else:
    	print("funktionen fungerar ej")


def test_set_data():

class Node:
		def __init__(self, init_data):
      		self.data = init_data
      		self.next = None
test_init = 1
test_node = Node(test_init)
newdata = 2

test_node.set_data(newdata)

if test_node.data == newdata
	print("Funktoinen fungerar")
else:
	print("Funktionen fungerar inte")


def test_set_next():

class Node:
	def __init__(self, init_data):
		self.data = init_data
      	self.next = None

test_init = 1
test_node = Node(test_init)
new_next = 2

test_node.set_next(new_next):

if test_node.next == new_next:
	print("Funktoinen fungerar")
else:
	print("Funktionen fungerar inte")



