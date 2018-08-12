#of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 

# of two lists using set() method
def intersection_set(lst1, lst2):
    return list(set(lst1) & set(lst2))
 
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

# driver code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))
print(intersection_set(lst1, lst2))
''' output:
	[9, 11, 26, 28]
	[9, 26, 11, 28]'''
