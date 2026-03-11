list_num =[1,2,3,4,5,6,7,8,9,10,1,2,3]
unique_list =[]

for i in list_num:
    if i not in unique_list:
        unique_list.append(i)
print("new list after removing duplicate element is :", unique_list)

# other method to remove duplicate element from list using set
list_number2 =[1,2,3,4,5,6,7,8,9,10,1,2,3]
unique_list2 = list(set(list_number2)) 

print("new list after removing duplicate element is :", unique_list2)

# one more method to remove duplicate element from list using dictionary
list_number3 =[1,2,3,4,5,6,7,8,9,10,1,2,3]
unique_list3 = list(dict.fromkeys(list_number3))
print("new list after removing duplicate element is :", unique_list3)