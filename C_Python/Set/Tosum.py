# Find two numbers whose sum is 10.


arr = [2,6,4,7,9,9,1,8,5,5]

pairs_list = []
no_duplicate_arr = list(set(arr))
print(type(no_duplicate_arr))
for i in range(0,len(no_duplicate_arr)):
    for j in range(i+1,len(no_duplicate_arr)):  # why are i+1  when the i take the from 0 give the reapited pairs  while take 1 not take the reapited paris 
        pairs = no_duplicate_arr[i]  + no_duplicate_arr[j]
        if pairs == 10 :
            pairs_list.append([no_duplicate_arr[i] ,no_duplicate_arr[j]])
print(pairs_list)