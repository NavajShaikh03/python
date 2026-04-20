# . Write a Python program to find the largest odd number in a given list of integers.
# Sample Data:
# ([0, 9, 2, 4, 5, 6]) ans 9
# ([-4, 0, 6, 1, 0, 2]) ans 1

lst = ([0, 9, 2, 4, 5, 6])
# print(type(lst))
# maxno = max(lst)
# if maxno % 2 !=0:
#     print("odd number:",maxno)
# else:
#     print("Even",maxno)

# other way to solve problem
    
largestOdd=0
for i in lst :
    if i % 2 !=0:
        if largestOdd < i:
            largestOdd = i
print("largestOdd number from list is : ",largestOdd)
            
    