tup = (43,54,76,98,90,34,23,20,3,4,2,1,0)

first_smallest  = float('inf')    # it means greatest number like infinity and use negative sign it means -infinity
second_smallest = float('inf')

for i in tup:
    if i< first_smallest:
        second_smallest = first_smallest
        first_smallest = i
    elif( i < second_smallest and first_smallest < i):
        second_smallest = i
print(first_smallest)
print(second_smallest)