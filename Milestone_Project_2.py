class Stack:
	def __init__(self):
		self.item=[]
	def push(self,item):
		self.item.append(item)
		print(self.item)
	def pop(self):
		try:
		 	return self.item.pop()
		except IndexError:
			print("there is an error")
			
	def peek(self):
		n=len(self.item)
		return self.item[n-1]

stack=Stack()
stack.push('nani')
stack.push('12')
stack.push('vicky')
stack.push(8)
stack.push(9)
stack.pop()






'''
output:
['nani']
['nani', '12']
['nani', '12', 'vicky']
['nani', '12', 'vicky', 8]
['nani', '12', 'vicky', 8, 9]
9
9
8
8
8
8
8
vicky
12
nani
there is an error
None

'''
