str=input("enter name\n")
rev=str[: : -1]
if str==rev:
	print("the string is palindrome")
else:
	print("the string is not a palindrome")