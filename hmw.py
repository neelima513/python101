def enumerate(sequence, start=0):
	n = start
	for elem in sequence:
		yield n, elem
		n= n+1
		print(n,elem)
