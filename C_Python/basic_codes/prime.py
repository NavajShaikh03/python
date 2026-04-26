number = int(input("Enter the number for check prime or not :"))
for i in range(1,number-1):
    if number %  i == 0 or number % i != 0:
        print("number is not prime")
    
print("number is prime")
 