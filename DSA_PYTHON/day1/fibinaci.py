n = int(input("Enter the number "))
a, b = 0 ,1
print(a,b ,end="")
for i in range(n):
    c = a+b
    print(c)
    a , b = b , c
    print(a,b ,end="")
    
