# number = int(input("Enter the large number for addition: "))
# sum=0
# while(number > 0):
#         fibonacci = number % 10
#         sum = sum + fibonacci
#         number =number // 10
# print(sum)

# number = input("Enter the large number for addition: ")
# total =0
# for i in number:
#     total=total + int(i)
# print(total)

# Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci series:")
while a < n:
    print(a, end=" ")
    a, b = b, a + b
