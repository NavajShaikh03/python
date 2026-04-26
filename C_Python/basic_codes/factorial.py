num = int( input("Enter the number for factorial:"))
factorial = 1
while (num>0):
    factorial = factorial * num
    num = num -1     #  number subtraction by one after multiplication to factorial number  
print(factorial)