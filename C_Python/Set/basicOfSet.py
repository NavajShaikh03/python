# Python Set:
# A Set is a collection of unique elements.
# Sets are written using curly braces {}.
# Sets are mutable (elements can be added or removed).
# Sets are unordered (elements have no fixed position).
# Sets do not allow duplicate values.
# Sets do not support indexing or slicing.
# Sets are iterable, so they can be used with a for loop.
# Set elements must be immutable (hashable), such as integers, strings, tuples, etc.
# Lists, dictionaries, and other sets cannot be elements of a set because they are mutable.

# Most Important Methods of set:
# Method	      -->   Description
# add(x)	      -->   Adds an element to the set
# update(iterable)-->	Adds multiple elements
# remove(x)	      -->   Removes an element (raises error if not found)
# discard(x)	  -->   Removes an element (no error if not found)
# pop()	          -->   Removes and returns a random element
# clear()	      -->   Removes all elements
# copy()          -->   Returns a shallow copy
# union()         -->	Returns union of sets
# intersection()  -->	Returns common elements
# difference()	  -->    Returns elements in first set but not second
# symmetric_difference()	-->Returns elements in either set but not both
# issubset()   -->  Checks if set is a subset
# issuperset() -->	Checks if set is a superset
# isdisjoint() -->	Checks if sets have no common elements

# practice 

s = {2,34,56,342,253}   #  this sample set

s2 = {23,34,23,2,23,53,1}

# print(type(s))

# s.add(3333)  #  add the element
# print(s)

# s.update([343334])
# print(s)

# s.remove(34)     # if key are not sound give  the error 
# print(s)

# s.discard(3333) # same as the remove method but one different if key are not found then not give the error 

# print(s)

# u =s.union(s2)

# print(u)

i = s.intersection(s2)

s.update([000000])
print(s)

copy_of_set = s.copy()
print(copy_of_set)

print("\n this is two set and its difference:")
print(s)
print(s2)
difference_btn = s.difference(s2)   #  return element in first set but it element not present in second
print(difference_btn)

symmetric = s.symmetric_difference(s2)    #  Returns elements in either set but not both 
print(symmetric)


print("\n")

print(s.issubset(s2))                  # if check the subset of set s2 if not print false

print(s.issuperset(s2))                # all element of set s is present in s2 if yes print true

print(s.isdisjoint(s2))               # if check the no common element 