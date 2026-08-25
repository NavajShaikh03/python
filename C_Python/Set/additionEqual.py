# check the addition of equal to 100 give pairs of number 

numbers = {10, 20, 30, 40, 50, 60, 70, 80}
numbers_list = list(numbers)

target_sum =int(input("enter the number :"))
pairs =[]

for i in range(0,len(numbers_list)):
    for j in range(i+1,len(numbers_list)):
        
        pair_of_addition = numbers_list[i] + numbers_list[j]        
        if pair_of_addition == target_sum :
            pairs.append([numbers_list[i],numbers_list[j]])
            
    # same number addition pairs 
    sameNo_addition = numbers_list[i] + numbers_list[i]
    if sameNo_addition == target_sum:                      # this condition execute end of the loop it give the same number pairs addition 
        pairs.append([numbers_list[i], numbers_list[i]])
    
    # same number is itself addition of two numbers 
    if target_sum == numbers_list[i]:
        pairs.append([numbers_list[i]])

print(f"your number is {target_sum} pairs of addition is :",pairs)
            