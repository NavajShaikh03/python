originalList = ["2","6","5","7","4","1","6","8"]      # string integer 

firstEven = 0
firstOdd = 0
for i in range(len(originalList)):
    if int(originalList[i]) % 2 == 0:
        firstEven= firstEven+int(originalList[i])
        break                                       # when the key are found then break the loop
for odd in range(len(originalList)):
    if int(originalList[odd]) % 2 != 0:
        firstOdd=firstOdd+int(originalList[odd])
        break                                      # when key are found then break the loop
    
print("first even no. from list is :",firstEven)
print("first odd in the list is :",firstOdd)