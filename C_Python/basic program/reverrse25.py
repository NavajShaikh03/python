# number = int(input("Enter the large number for reverse:"))
# reverse = 0
# while number > 0:
#     last_digit = number % 10
#     reverse = reverse * 10 + last_digit
#     number = number // 10
# print(reverse)


# # same as other method

# number = input("Enter the number :")
# print(number[::-1])


number2 = input("enter the large number for reverse order :")
reverse2 = ""
for i in number2:
    reverse2 = i + reverse2
print(reverse2)
