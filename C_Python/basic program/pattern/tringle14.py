i=1 
while(i<=4):
    j=1
    while(j<=i):
        print(" " * (5-i)  ,  "*" * i)
        j+=1
    print()
    i+=1