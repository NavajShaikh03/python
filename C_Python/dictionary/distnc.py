# 8. Write a Python program to print all distinct values in a dictionary.

# distinct means unique values

dict1 = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":4,
    "F":2,
    "G":1,
}

print(set(dict1.values()))


unique_value =[]
for value in dict1.values():     
    if value not in unique_value:    
        unique_value.append(value)      # add the unique values 
    else:
        print("Repeated values in dictionary :",value)    #  print the repeated values 
print("unique value is :",unique_value)