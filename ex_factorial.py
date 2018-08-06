def fact(n)=4
fact=1
for i in range(1,n+1):
	fact=fact*i
	print("the factorial of",n,"is",fact)

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


weight=float(input("enter the weight"))
height=float(input("enter the height"))
print(weight/(height*height)