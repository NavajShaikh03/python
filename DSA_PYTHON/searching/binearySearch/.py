'''
a temperature sensor records the value sorted by time 
above a certain temp machine shut down
find the first time the index when the temp exceed the certain temp limit

i/p: 
temp = sorted list of integers
limit = integers

o/p:
index of the first temp exceed the limit
'''

def first_exceeding_temp(temp,limit):
    left = 0
    right = len(temp)-1
    
    while left <= right:
        mid = (left + right)//2
        
        if temp[mid] == limit:
            return mid
        
        elif temp[mid] < limit:
            left = mid+1
        else:
            right = mid-1
    return -1

temp = [21,34,56,67,78,89,98]
limit = 5-1

result = first_exceeding_temp(temp,limit)

if result != -1:
    print("The first exceed the temprature at index is",result)
else:
    print("The first not exceed the temprature at index is",result)
        
    
    