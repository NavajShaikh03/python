number = int(input("Enter the large number for factorial: "))
factorial = 1
while (number > 0):
    last_digit = number % 10
    factorial = factorial * last_digit
    number = number // 10
print(factorial)



number1 = int(input("Enter the large number for factorial: "))
factorial = 1
for i in range(len(str(number1))):
    last_digit = number1 % 10
    factorial = factorial * last_digit
    number1 = number1 // 10
print(factorial)


#factorial

def fact(n):
    