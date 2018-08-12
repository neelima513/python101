#square root

num=int(input('enter a number:'))
num_squrt=num**0.5
print(num_squrt)
'''
input: enter a number:4
output:2.0
input:enter a number:5
output:2.23606797749979'''

#area of triangle

a=int(input('enter the side of a:'))
b=int(input('enter the side of b:'))
c=int(input('enter the side of c:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) **(1.0/2)
print('the area of the triangle is ',area)
'''
input:enter the side of a:5
	enter the side of b:4
	enter the side of c:2

output:the area of the triangle is  3.799671038392666

input:enter the side of a:4
	enter the side of b:7
	enter the side of c:8
output:the area of the triangle is  13.997767679169419'''



#quodratic equation
import cmath

a = float(input('\n\nEnter a: '))

b = float(input('Enter b: '))

c = float(input('Enter c: '))

d=(b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)

sol2 = (-b+cmath.sqrt(d))/(2*a)
print("the soluttions are :",sol1,sol2)

'''
input:  Enter a: 2
	Enter b: 5
	Enter c: -3
output:
	the soluttions are:(-3+0j) (0.5+0j)'''
	

#ex_5

print("\n\nMary had a little lamb.")
print("And everywhere that Mary went.")
print("." * 20)  # what'd that do?
#it prints . as 20 times
'''
....................'''

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that "end" parameter at the end. (end=' ')
# try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end='\t')
print(end7 + end8 + end9 + end10 + end11 + end12)


'''output:

using (end=' ')
....................
Cheese Burger


using (end='\n') or removing (end=' ')
....................
Cheese
Burger


using (end='\t')

....................
Cheese  Burger'''


