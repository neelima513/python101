'''input:python ex_if_elif.py 4
output:4 is grater than 0'''
import sys
pgm_name=sys.argv[0]
print(pgm_name)
num=int(sys.argv[1])
if num>0:
	print(num,"is grater than 0")
elif num<0:
	print(num,"is less than 0")
else:
	print(num,"is equal to 0")
