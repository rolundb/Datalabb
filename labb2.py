
class ListQ:

 def __init__(self):
 	self.the_list = []

 def put(self):
 	self.the_list.append(self)

 def get(self):
 	self.the_list.pop()

 def isEmpty(self):
 	if len(self.the_list) == 0:
 		return True
 	else:
 		return False

	

#Test 1 
q = ListQ()

if q.isEmpty():
	print("q.isEmpty() ger rätt svar.")

else:
	print("q.isEmpty() ger FEL svar.")
