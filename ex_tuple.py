result=[]
l1=[1,0,0,0]
l2=[0,1,0,0]
l3=[0,0,1,0]
l4=[0,0,0,1]
t=(l1,l2,l3,l4)
for row, list in enumerate(t):
	print("these are rows:",row)
	for col,item in enumerate(list):
		print("these are cols:",col)
		if(row == col):
			t=(row,col)
			result.append(t)
			print(t)
'''output:
these are rows: 0
these are cols: 0
(0, 0)
these are cols: 1
these are cols: 2
these are cols: 3
these are rows: 1
these are cols: 0
these are cols: 1
(1, 1)
these are cols: 2
these are cols: 3
these are rows: 2
these are cols: 0
these are cols: 1
these are cols: 2
(2, 2)
these are cols: 3
these are rows: 3
these are cols: 0
these are cols: 1
these are cols: 2
these are cols: 3
(3, 3)'''
