number =(input("Enter the number for check palindrome:"))
revers = 0
while (int(number) > 0):
    last_digit = int(number) % 10
    revers = revers * 10 + last_digit
    number = int(number) // 10
print(f"Reverse number is :{revers}")
    
if number == (str(number)[::-1]):
    print("palendrome")
if number == revers:
    print("palendrome")
else:
    print("not palendrome")
    
    
    
    
# another method to check palindrome using function
def is_palindrome(n):
    return n == n[::-1]     
number1 = input("Enter the number for check palindrome:")
if is_palindrome(number1):
    print("palendrome")
else:
    print("not palendrome") 

# another method to check palindrome using recursion
def is_palindrome_recursive(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome_recursive(n[1:-1])
number2 = input("Enter the number for check palindrome:")
if is_palindrome_recursive(number2):
    print("palendrome")
else:
    print("not palendrome")
    

 