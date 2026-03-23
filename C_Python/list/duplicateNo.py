numbers = [1,2,3,4,3,2,3,3,4,2,2,2,1,67,676,567,56]

print("original list is : ",numbers)
duplicate_number = []
non_duplicate_number = []

for i in  numbers:
    if numbers.count(i) > 1 and i not in duplicate_number:
        duplicate_number.append(i)
            
    if i not in duplicate_number:
        non_duplicate_number.append(i)
        
print(" \n  duplicate number in list:",duplicate_number)
print(" \n non duplicate number in list:",non_duplicate_number)