arr = [4,6,7,6,8,9,7,8,8,3,5,2,1,7,3,4]

seen = set()
duplicate = set()

for i in arr:
    if i not in seen:
        seen.add(i)
        
    else:
        duplicate.add(i)
print("duplicate element in the array :",duplicate)