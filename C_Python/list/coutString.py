string = ["hello","mom","dad","mdm","mdm","mdm","mdm","mdm","mdm"]

count =0
for i in string:
    if len(i) >=2:
        if i[0]==i[-1]:   # check first and last character and if they are same then count will increase by 1
            count +=1
print(count)