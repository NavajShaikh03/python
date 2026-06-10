# finding the missing number from one set to other set and vice versa

set1 = {1,2,4,5,6,7,8,9}
set2 = {2,3,5,6,8,9}

for i in set1 :
    if i not in set2 :
        print("missing number of set2 compared to set3:",i)
print("\n")
for j in set2 :
    if j not in set1:
        print("missing number in set1 compared to set2 :",j)
print("\n")
        
# other method finding number

print("missing number of set1 :",set2 - set1)

print("missing number of set2 :",set1 - set2)

