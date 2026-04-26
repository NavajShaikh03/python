number1= int(input("Enter the number1:"))
number2= int(input("Enter the number2:"))
number3= int(input("Enter the number3:"))


if (number1 >= number2 and number1 >=number3 ):
    print(f"{number1} is the maximum number")
elif(number2 >= number1 and number2 >=number3):
    print(f"{number2} is the maximum number")
else:
    print(f"{number3} is the maximum number")
    
# onther method to find maximum number using function
def find_maximum(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    else:
        return c
number1= int(input("Enter the number1:"))
number2= int(input("Enter the number2:"))
number3= int(input("Enter the number3:"))
maximum_number = find_maximum(number1, number2, number3)
print(f"{maximum_number} is the maximum number")    
