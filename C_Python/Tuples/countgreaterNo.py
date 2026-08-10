tup = (35,45,97,54,85765,96,987,8763,3,2,5,5)
print(tup)
num = int(input("Enter any one number:"))
count =0
for i in tup:
    if i < num:
        count+=1
print(f"{num} grater numbers count:",count)
