#Queue
class Queue:
	print("*","queue","*")
	def __init__(self):
		self.items=[]
	
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items==[]
	def size_of(self):
		return len(self.items)
	def printqueue(self):
		for items in self.items:
			print(items)
			
q=Queue()
print(q.isEmpty())
q.enqueue('nandhu')
q.enqueue('nani')
q.enqueue('vicky')
q.enqueue('22')
q.enqueue('14')
q.printqueue()
q.dequeue()
q.printqueue()


'''output:
********** Queue **********
True
['nandhu']
['nani', 'nandhu']
['vicky', 'nani', 'nandhu']
['22', 'vicky', 'nani', 'nandhu']
['14', '22', 'vicky', 'nani', 'nandhu']
nandhu
nani
vicky
2


'''

