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
stack.peek()
print(stack.peek())
stack.pop()
stack.peek()
print(stack.peek())
stack.push(2)
stack.peek()
print(stack.peek())
stack.pop()
stack.push(5)
stack.peek()
print(stack.peek())
stack.pop()
print(stack.pop())
stack.pop()
print(stack.pop())
stack.pop()
print(stack.pop())
stack.pop()
print(stack.pop())
'''
output:
['nani']
['nani', '12']
['nani', '12', 'vicky']
['nani', '12', 'vicky', 8]
['nani', '12', 'vicky', 8, 9]
9
8
['nani', '12', 'vicky', 8, 2]
2
['nani', '12', 'vicky', 8, 5]
5
8
12
there is an error
None
there is an error
there is an error
None


'''
