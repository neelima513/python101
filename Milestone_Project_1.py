#MILESTONE PROJECT 1
#====================
class Milestone_1:
	def __init__(self,w,h,n,s,sen1,sen2):
		self.w=w
		self.h=h
		self.n=n
		self.s=s
		self.sen1=sen1
		self.sen2=sen2

	#2.reverse a string
	'''
	input: nani
	output: inan'''	
	
	
	def reverse(self):
		rev = self.s[::-1]
		print("reverse of string is:",rev)
	
	#3.palindrome
	'''input:enter name:
		madam
	    output:the string is palindrome'''
	
	
	def palindrome(self):
		rev=self.s[: : -1]
		if self.s==rev:
			print("the string is palindrome")
		else:
			print("the string is not a palindrome")
	
	
	#4.bmi calulator


	'''input:enter the weight 39
	enter the height 5.2
   	outpu:
	1.442307692307692'''

	
	def bmi(self):
		print(self.w/self.h**2)
	

	#8.factorial
	'''output:the factorial of 3 is 1
		  the factorial of 3 is 2
		  the factorial of 3 is 6'''

	
	def fact(self):
		fact=1
		for i in range(1,self.n+1):
			fact=fact*i
			print("the factorial of",self.n,"is",fact)
	#1.vowels
	'''output:No. of vowels: 4'''

	def vowel(self):
		vowel=['a','e','i','o','u' or 'A','E','I','O','U']
		count=0
		for i in self.sen1:
			if i in vowel:
				count+=1
		print("No. of vowels:",count)

	#6.removing puncuations	

	'''input:hello","\t",@#world
	   output:hello   world'''


	def punctuation(self):
		punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
		no_punctuation=""
		for i in self.sen2:
			if i not in punctuation:
				no_punctuation=no_punctuation+i
		print(no_punctuation)
	#5.print * in a triangle pattern

	'''output:
		 *

		 * *

		 * * *'''





	def pattern(self):
		for i in range(0,self.n):
			for j in range(0,i+1):
				print(" *",end="")
			print("\n")
	#7.sorting and split
	'''input:ai this is
	   output:['hai', 'this', 'is']
		  ['hai', 'is', 'this']'''

	
	def sort(self):
		word=self.sen1
		sen1=word.split()
		print(sen1)
		sen1.sort()
		print(sen1)
	
	
	


obj_milestone=Milestone_1(39,5.2,3,'amma',"hai this is",'hello","\t",@#world')
obj_milestone.reverse()
obj_milestone.palindrome()
obj_milestone.bmi()
obj_milestone.fact()
obj_milestone.vowel()
obj_milestone.punctuation()
obj_milestone.pattern()
obj_milestone.sort()
