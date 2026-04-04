a = 20
b = 20
gmean1 = (a*b)/(a+b)
print(gmean1) 

def calculateGmean(a,b):    # this function it is use multiple times with same logic
    mean = (a*b)/(a+b)
    print(mean)
    
a = 10 
b = 80
calculateGmean(a,b)

# Greater number

def GreaterNo(a ,b):
    if (a > b):
        print("a is greater then b")
    else:
        print("b is greater then a ")
a = 10 
b = 20
GreaterNo(a , b)