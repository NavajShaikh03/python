# 40. Find out square of no. using lambda functionQ

square  = lambda s : s**2
print(square(5))

# Find out largest number between two 
# numbers using lambda function

largest = lambda x , y :  x if x> y else y
d = largest(10,20)
print(d)


# Q42. Find out largest number between three numbers using lambda function
l = lambda n ,s , m : n if n > s and n > m  else s if s >m and s >n else m
print(l(10,20,30) )
     
     
