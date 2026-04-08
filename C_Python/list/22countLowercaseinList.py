list_of_word = ["Red","Green","Blue","White"]   # count the total lower case from the list  
count =0
for word in list_of_word:
    for character in word:
        if  character.islower():
            count=count + 1
print(count)