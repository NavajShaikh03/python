# list comprehension are used creating new lists from other iterables like lists 
#tuples dictionaries sets and even in array and string

lst = [i  for i in range(4)]
print(lst)

lst = [i  for i in range(10) if i%2 ==0]
print(lst)