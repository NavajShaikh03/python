# not repeated the duplicate
# order not in set
# indexing are not allowed
s = {6,7}
print(s) 
s.add(8)     # add the element in set
print(s)
s.remove(7)  # remove the element from set if element is not found then get error 
print(s)
s.discard(8) # it also remove the element from set safely
del s        # delate the set 



info = {"carla",19,False,5.8,44}
print(info)
h = set()
print(type(h))
for value in info:
    print(value)
    
# method of set

s1 = {1,2,3,4,6}
s2 = {1,2,3,4}
print(s1.union(s2))
print(s1.update(s2))
print(s2.issubset(s1)) # if yes then true
 
cities1 = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}

cities3 = cities1.symmetric_difference(cities2)   #  not get same element 
print("common cities is :",cities3)

cities4 = cities1.intersection(cities2)    # to take the common element
print("repeated cities is :",cities4)

cities5 = cities1.intersection_update(cities2)
print(cities5)

cities6 = cities1.isdisjoint(cities2)    
print(cities6)                          # all element of both set are different then print false otherwise true
