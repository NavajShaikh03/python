# number = int(input("enter the large number for reverse order :"))    # revese the itself number
# reverse = 0
# while(number > 0):
#     last_digit = number % 10
#     reverse = reverse * 10 + last_digit
#     number = number // 10
# print(reverse) 

# # another method to reverse the number
# number1 = int(input("enter the large number for reverse order :"))
# reverse1 = 0
# for i in range(len(str(number1))):
#     last_digit = number1 % 10
#     reverse1 = reverse1 * 10 + last_digit
#     number1 = number1 // 10
# print(reverse1)

# # another method to reverse the number using string
# number2 = input("enter the large number for reverse order :")
# reverse2 = ""
# for i in number2:
#     reverse2 = i + reverse2
# print(reverse2)

# another method to reverse the number using slicing
number3 = input("enter the large number for reverse order :")
reverse3 = number3[::-1]
print(reverse3)

# another method to reverse the number using recursion
def reverse_number(n):
    if len(n) == 0:
        return n
    else:
        return n[-1] + reverse_number(n[:-1])
number4 = input("enter the large number for reverse order :")
reverse4 = reverse_number(number4)
print(reverse4)

# another method to reverse the number using join and reversed function
number5 = input("enter the large number for reverse order :")
reverse5 = ''.join(reversed(number5))                              #  method
print(reverse5)
