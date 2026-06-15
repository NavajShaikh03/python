number = {3,5,4,2,9,8,45,85,93}

copy_number = number.copy()     # create the copy set and perform operation
print(copy_number)

for i in range(0,2):  # take the range 
   copy_number.remove(max(copy_number))   # remove the two greater number from set 
print(copy_number)
print("Third greater number from set is :",max(copy_number))