n = int(input("Enter number of element for count:"))  # take  input  from the user 
numbers = []

for i in range(n):
    num = input("Enter number:")
    numbers.append(num)

lower = input("Enter lower number from list:")    # this variable is take the lower value 
high = input("Enter the higher number from list:")   # this take the grater value from list 

count =0
for i in numbers:
    if lower < i < high:
        count +=1
        
print("count btn in list:",count)     # count the number the in btn l and h 

# other way  built function

n2 = input("")










