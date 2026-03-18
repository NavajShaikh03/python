l1 = [13,4,7,34,76]
l2 = [13,45,4,34,3]

for i in range(len(l1)):  # find the similar number from list 
    if l1[i] in l2:
        print(l1[i])
        
# other way

print(set(l1) & set(l2))


# other way
common = [x for x in l1 if x in l2]
print(common)

