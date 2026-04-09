for i in range(6):
    print(i)
    # if i==4:
    #     break
else:
    print("Sorry no element present")   # when break the for loop this content cot execute 
    

# while loop
i = 1
while i < 9:
    print(i)
    i=i+1
    if i == 7:
        break
else:
    print("Sorry for element not present")
    
# one more example

for x in range(5):
    print("iteration no {} in for loop".format(x+1))    
else:
    print("Else block in loop ")
print("Out of loop")