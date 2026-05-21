print("Inverted Pyramid\n ")

for i in range(5):
    print(" " * i,end= "  ")    
    x = '* ' * (5-i)
    # print(x.center(10))  # this line work like end = "" 
    print(x)