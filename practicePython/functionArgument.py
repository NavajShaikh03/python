# # there are four types of argument that we can provide in a function:
# 1) Default argu
# 2)keyword  argu
# 3)variable length argu
#  a) arbitrary Argument
#  b) keywordArguments
# 4)required argu


# def average(a,b):
#     print("The average is ",(a+b)/2)
# average(5,6)

def average(*numbers):   # arbitory argument when call the its then take the list 
    sum = 0
    for i in numbers:
        sum = sum  + i
    print("Average is :",sum / len(numbers))
average(1,2,3,4,5,6,7,8,9)


def name(**name):   # keyword arguments
    print("Hello,",name["nname"],name["mname"],name["lname"])
name(mname = "mahi",nname ="navaj",lname = "Lets go")