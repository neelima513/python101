#factorial
'''the factorial number of 7 is: 5040'''

def factorial(n):
	factorial = 1
	if n<0:
		print("factorial number doesnot exits")
	elif n==0:
		print("the factorial of 0 is 1")
	else:
		for i in range(factorial,n+1):
			factorial = factorial * i
		print("the factorial number of",n,"is:",factorial)
n = 7
factorial(n)

#bmi calculator
'''input:enter the weight 39
	enter the height 5.2
output: 
	1.442307692307692
weight=float(input("enter the weight"))
height=float(input("enter the height"))
print(weight/(height*height))