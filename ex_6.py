default_order="{},{}and{}".format('john','bill','sean')
print('\n---default order---')
print(default_order)


positional_order="{1}, {0}and {2}".format('john','bill','sean')
print('\n--positional_order--')
print(positional_order)

keyword_order="{s},{b}and{j}".format(j='john',b='bill',s='sean')
print('\n----keyword_order----')
print(keyword_order)

'''sample output:
  
  ---default order---
john,billandsean

--positional_order--
bill, johnand sean

----keyword_order----
sean,billandjohn'''


  
  
