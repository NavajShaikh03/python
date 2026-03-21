element = [1,2,3,4,5,6,7]
copy_element = element.copy()  # copy the list to avoid changing the original list

print("original list:",copy_element)
if len(element) >=2: # check if the list has at least 2 elements to swap
    element[0],element[-1] = element[-1],element[0]
    
print("swapped the last and first element in list:",element)