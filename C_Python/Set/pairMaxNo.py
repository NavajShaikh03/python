set1 = {1,2,3,4,5,6,7,8,9,10}

set_to_list = list(set1)

previous_sum = 0
max_pairs = []
for i in range(0,len(set1)) :
    for j in range(i+1,len(set1)):
        current_sum = set_to_list[i] + set_to_list[j]
        
        if current_sum > previous_sum:
            previous_sum = current_sum
            max_pairs=([set_to_list[i] , set_to_list[j]])    # not store the always value store value in list temporary
print("max pairs from the arr:",max_pairs)
print(i,j)
print("max pairs addition is :",i+j)            