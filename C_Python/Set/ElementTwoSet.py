# remove the common element in both set .

set1 = {1,3,4,2,4,6,8,4,3,9,345,345,352,34}
set2 = {4,6,3,8,9,1,4,5,6,7,93,34,223,243}

# for i in set1 :
#     if i in set2:
#         set2.remove(i)
# print(set2)

common = set1 & set2 
print(common)

different_element_both_set = set1 ^ set2    # this ^ symbol is symmetric_difference

print(different_element_both_set)    # delete common element both set