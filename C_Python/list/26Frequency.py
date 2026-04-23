# . Write a Python program to get the frequency of elements in a given list of lists.
# Original list of lists: [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

lst= [[1, 2, 3, 2],[4, 5, 6, 2],[7, 8, 9, 5]]

new_list= []              # for convert sub_list to one list
for i in lst:
    for j in i:
        new_list.append(j)  # create new list add number one by one 
for num in set(new_list):
    print(num,":",new_list.count(num))   # this use the count frequency of number
    
    