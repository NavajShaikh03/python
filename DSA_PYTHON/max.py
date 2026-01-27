def maxOfThree(n1,n2,n3):
    if(n1 > n2 and n1 > n3):
        print(F"{n1} is greater")
    elif(n2> n1 and n2 > n3):
        print(f"{n2 }is greater")
    else:
        if(n1==n2==n3):
            print("All three number are equal")
        else:
            print(f"{n3} is greater")
n1 = input("Enter the number n1:")
n2 = input("Enter the number n2:")
n3 = input("Enter the number n3:")

maxOfThree(n1,n2,n3)
