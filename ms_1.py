#2. reverse a string


'''
input: nani
output: inan'''

str="nani"
str_length=len(str)
reversed_str=str[-1:-(str_length+1):-1]
print(input(str))
print(reversed_str)





# 3.palindrome or not

'''enter name
madam
the string is palindrome'''

print(" checking the given string is palindrome or not") 
str=input("enter name\n")
rev=str[: : -1]
if str==rev:
	print("the string is palindrome")
else:
	print("the string is not a palindrome")

#4.BMI calulator

'''input:enter the weight 39
	enter the height 5.2
   outpu:
	1.442307692307692'''

weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
print(weight/height*height)



#5. print * in a triangle pattern 


'''input:enter num of rows 3
output:
 *

 * *

 * * *'''
print("printing *")
def pattern(num):
	for i in range(0,num):
		for j in range(0,i+1):
            		print(" *",end="")
		print("\n")

# 7.Take a sentence, sort words in a sentence in an alphabetical order use string split() and string sort functions

def sort(s):
	print("spliting and sorting of words in a sentance")
	word.sort()
	for i in word:
		print(i)
s=("this is my world")
word=s.split()
sort(s)
# 8. factorial of a number

'''the factorial of 4 is 1
the factorial of 4 is 2
the factorial of 4 is 6
the factorial of 4 is 24'''

print("\n\n factorial of a given number")
def fact(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
		print("the factorial of",n,"is",fact)
n=4
fact(n)


#1.vowels
print("\n\n vowels in a string")

def vowel(str):
    str="nandhini reddy"
    vowel=['a','e','i','o','u' or 'A','E','I','O','U']
    count=0
    for i in str:
        if i in vowel:
           count+=1
    print("No. of vowels:",count)

vowel(str)

#6.removing puncuations
print("\n\n removing the puncuations in a sentance")

def punct(str):
    punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    no_punct=""
    for i in str:
        if i not in punct:
           no_punct=no_punct+i
    print(no_punct)
str=("this is *!my  #$ Wor*l@d")
punct(str)
