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
# add() 
# update()
# remove()
# discard()
# pop()
# clear()
# copy()
# union()
# intersection()
# difference()
# symmetric_difference()


# practice 

s = {2,34,56,342,253}   #  this sample set

print(type(s))

s.add(3333)  #  add the element
print(s)

s.update([343334])
print(s)

s.remove(34)     # if key are not sound give  the error 
print(s)

s.discard(3333) # same as the remove method but one different if key are not found then not give the error 

print(s)