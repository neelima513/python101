a=input('enter a value:')
b=input('enter b value:')
c=input('enter c value:')
if a>b or a>c:
	print('a is big:',a)
	if b>a and b>c:
		print('b is big:',b)
else:
	print('c is big:',c)
'''input:
enter a value:48
enter b value:20
enter c value:15

output:
a is big: 48'''
