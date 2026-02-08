def number(n):
    value=1
    for i in range(1,n):
        print(value,end=" ")
        value = value *2
n = int(input("Enter the no. for 2 series:"))
number(n)