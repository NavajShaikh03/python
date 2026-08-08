# A tuple is an ordered, immutable (cant changed ) and indexed collection in python
# A built in data type that lets us create immutable sequences of values 
# tuple have two methods because they are immutable
# faster than lists and used for fixed data
tup  = () 
print(type(tup))   # tuple

tup2 = (1)  
print(type(tup2))  # int


# slicing in tuple 

tup = (1,2,3,4)
print("tuple slicing :",tup[1:3])

# method 1
print(tup.count(2))

# method 2
print("index of tuples :",tup.index(2))

# wap to ask the to enter names of their 3 favorite movies & store them in a list .

movies = []

mov1 = input("Enter the 1st movie :")
mov2 = input("Enter the 2nd movie :")
mov3 = input("Enter the 3rd movie :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print("all movies :",movies)