numbers = [1,2,3,4,3,2,3,3,4,2,2,2,1,67,676,567,56]
duplicate_number = []

for i in  numbers:
    if numbers.count(i) > 1 and i not in duplicate_number:
        duplicate_number.append(i)
        numbers.remove(i)
print("duplicate number in list:",duplicate_number)
print(" non duplicate number in list using set:",numbers)