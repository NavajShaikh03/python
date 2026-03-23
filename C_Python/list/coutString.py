string = ["hello","mom","dad","mdm","mdm","mdm","mdm","mdm","mdm"]   #  string ogf words

count =0
for i in string:   # in sting if  first an last character are same then count will increase by 1
    if len(i) >=2:
        if i[0]==i[-1]:   # check first and last character and if they are same then count will increase by 1
            count +=1
print(count)