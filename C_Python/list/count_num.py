n = int(input("Enter number of element for count:"))  # take 
numbers = []

for i in range(n):
    num = input("Enter number:")
    numbers.append(num)

lower = input("Enter lower number from list:")
high = input("Enter the higher number from list:")

count =0
for i in numbers:
    if lower < i < high:
        count +=1
        
print("count btn in list:",count)

# other way