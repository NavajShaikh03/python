number1= int(input("Enter the number1:"))
number2= int(input("Enter the number2:"))
number3= int(input("Enter the number3:"))


if (number1 >= number2 and number1 >=number3 ):
    print(f"{number1} is the maximum number")
elif(number2 >= number1 and number2 >=number3):
    print(f"{number2} is the maximum number")
else:
    print(f"{number3} is the maximum number")