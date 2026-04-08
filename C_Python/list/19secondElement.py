# Write a Python program to find the second smallest number in a list

# smallest_element = [1,1,2,3,1,2,0,3,4,5,6,7,8,9,10]
# copy_list_data = set(smallest_element.copy())
# print(copy_list_data)
# print("First smallest element in list is :",min(copy_list_data))
# copy_list_data.remove(min(copy_list_data))                       # this logic is correct but data remove from list ???
# print("Second smallest element in list is :",min(copy_list_data))
# print("\nOriginal list is after perform operation",smallest_element)


#  other way
data = [1,2,3,4,5,6,4,4,2,11,65]
uniq_data = set(data)
set_to_listData =list(uniq_data)

sort_data =set_to_listData.sort()
print(sort_data)