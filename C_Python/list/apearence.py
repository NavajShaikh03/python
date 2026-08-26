# Find all numbers that appear more than once.

numbers = [4, 7, 2, 4, 9, 7, 3, 2, 8, 4, 9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        
        if numbers[i] == numbers[j]:   # compare the number take one number and compare with  next other numbers 
            print(numbers[i])
            break
        