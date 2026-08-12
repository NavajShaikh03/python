# Given a tuple of integers, find the first and second largest elements in one traversal.

tup = (45,36,35,35,36,98,75,38,100)
first_largest = 0
second_largest =0
for i in tup:
    if i > first_largest:
        first_largest = i
    else:
        second_largest=first_largest
print(first_largest)
print(second_largest)
