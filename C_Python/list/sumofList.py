lists= [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

sum_list =[]
for i in lists:
    addition_of_list_element = sum(i)
    sum_list.append(addition_of_list_element)    
if max(sum_list):
    index_no =sum_list.index(max(sum_list))
    print(lists[index_no])
    
    
# other

result = max(lists, key =lambda x: sum(x))
print(result)
print(f"sum of height list {result}: {sum(result)}")


# other way

max_sum = 0
max_list  =[]

for lst in  lists:
    if sum(lst) > max_sum:
        max_sum = sum(lst)
        max_list = lst
        
print(f"list with maximum sum :{max_list} and sum is :{max_sum}")