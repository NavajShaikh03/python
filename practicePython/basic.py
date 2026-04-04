# print("Hi mahi")   # function to print the output
# print(5)
# print("Bye")
# print(5+5)

# # Hey PLEASE dont re,ove this line
# print("Hey I am a learning python \n and i am loving it ")
# print("mahi",6,sep="---",end="***")


# # vaibles and data types

 
# n1 = 65
# n2   = 56

# print(n1+n2)
# print(n1-n2)
# print(n1*n2)
# print(n1/n2)

# # a =  input("Enter your name :")
# # print("My name is ",a)

# # x = input("Enter first name :")
# # y = input("Enter the second name :")

# # print(x + y)


# #   condition statement

# a  = int(input("Enter the age :"))
# print("Your age is :",a)

# if (a > 18):
#     print("You can drive")
# else:
#     print("You can not drive")
    
# applePrice = 10 
# budget = 200

# if (budget - applePrice > 50 ):
#     print("Alexa, add 1 kg Apples to the cart.")
# elif(budget - applePrice > 70 ):
#     print("Its okay you can buy ")
# else:
#     print("Alexa, do not add Apples to the cart.")
    
#  Esersies

# import time     #   this is modules of times 
# timestamp = time.strftime('%H:%M:%S')    # print the your time 

# print(timestamp)

# timestamp = time.strftime('%H')
# print(timestamp)                  # this print hours 

# timestamp = time.strftime('%M')
# print(timestamp)                  # this is print the minutes

# timestamp = time.strftime('%S')
# print(timestamp)                  # this is print the seconds


# loops

# name = "Abisheck"

# for i in name:
#     print(i)
#     if(i == "b"):
#         print("this is something special!")
        
# colors = ["Red","Green","Blue","Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
        
# for k in range(1, 100+1,2):
#     print(k)
    
# # while loop 

# i = int(input("Enter the number"))
# while(i<3):
#     print(i)
#     i =i + 1
# print("Done with the loop")

for i in range(12):
    if(i == 10):
        print("Skip the iteration ")
        continue
    print("5 X" ,i+1,"=" , 5 *(i+1) )
    
i =0
while True :
    print(i)
    i = i +1
    if(i % 100 == 0):
        break
