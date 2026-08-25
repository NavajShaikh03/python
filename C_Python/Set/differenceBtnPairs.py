numbers = {10,9,8,7,6,5,4,3,2,1,44,3,32,53,3,53,23,3,4,79,46,9,5,79}

numbers_list = list(numbers)

difference_target = int(input("enter the your difference numbers btn two numbers :"))
pairs = []

for i in range(0,len(numbers_list)):
    for j in range(i+1,len(numbers_list)):
        
        # difference variable
        difference_number = numbers_list[i] - numbers_list[j]
        
        if difference_target == difference_number or -(difference_target) == difference_number:
            pairs.append([numbers_list[i],numbers_list[j]])
print(f"difference equal to you number {difference_target} pairs is :",pairs)