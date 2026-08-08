tup = (34,54,32,23,54,56,67,454,345)
max = tup[0]
min = tup[0]
for i in tup:
    if i > max:
        max = i
    elif( i < min):
        min =i
    
print("max number using tuple :",max)
print("min number using tuple :",min)
