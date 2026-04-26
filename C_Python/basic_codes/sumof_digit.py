number = int(input("Enter the large number for sum:"))
sum =0
while number>0:
    last_digit = number % 10
    sum = sum + last_digit
    number = number //10
print(sum)