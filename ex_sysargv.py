'''input: python ex_sysargv.py nani nandhu

output:ex_sysargv.py
['nani', 'nandhu']
this is my homework'''



import sys
pgm_name=sys.argv[0]
print(pgm_name)
arguments=sys.argv[1:]
count=len(arguments)
print(arguments)
print("this is my homework")
