numbers = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numbers)): # before find largest and smallest number in list we have to sort the list in ascending order
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j],numbers[i]

print("Largest number in list:",numbers[-1])
print("Smallest number in list is :",numbers[0])            

# other way 

largest = numbers[0]     #  consider the first number is smaller same as the smallest
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i
print("Largest number in list:",largest)
print("smallest numbers in list:",smallest)



numbers =[1,2,36,7,9,0,46,778,454]

print(max(numbers))
print(min(numbers))