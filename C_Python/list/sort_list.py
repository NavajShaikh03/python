number = [1,3,5,2,4,6,8,7,9,10]

for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i]> number[j]:
            number[i],number[j] = number[j] , number[i]
            
print("Sorted list:",number)    