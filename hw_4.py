#Enumerate

grocery = ['bread', 'milk', 'butter']

enumerateGrocery = enumerate(grocery)


print(type(enumerateGrocery))



print(list(enumerateGrocery))


enumerateGrocery = enumerate(grocery, 10)

print(list(enumerateGrocery))

'''
input:<class 'enumerate'>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]'''


#ex-2:
grocery = ['bread', 'milk', 'butter']


for item in enumerate(grocery):
 
	print(item)

print('\n')

for count, item in enumerate(grocery):

	print(count, item)

print('\n')

for count, item in enumerate(grocery, 100):

	print(count, item)

'''
input$output:
(0, 'bread')
(1, 'milk')
(2, 'butter')

0 bread
1 milk
2 butter

100 bread
101 milk
102 butter'''

#for loop

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum=0


for val in numbers:
	
	sum = sum+val

print("The sum is", sum)

'''
 Output: The sum is 48'''

#Range


print(list(range(0)))


print(list(range(10)))


print(list(range(1, 10)))

'''output:
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]'''

#List:
animal = ['cat', 'dog', 'rabbit']
animal.append('guinea pig')



print('Updated animal list: ', animal)

'''output:
Updated animal list:  ['cat', 'dog', 'rabbit', 'guinea pig']'''


#ex2:


animal = ['cat', 'dog', 'rabbit', 'guinea pig']



animal.remove('rabbit')



print('Updated animal list: ', animal)

'''output:
Updated animal list:  ['cat', 'dog', 'guinea pig']'''
















