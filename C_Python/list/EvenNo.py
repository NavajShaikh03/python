number = [1,2,3,4,5,6,7,8,9,10]
odd_number =[]
for odd in number:
    if odd % 2!=0:
        odd_number.append(odd)
print("odd number in list:",odd_number)

# other way 

numbers = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd numbers:", odd_numbers)