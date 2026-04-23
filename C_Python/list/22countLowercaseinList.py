list_of_word = ["Red","Green","Blue","White"]   # count the total lower case from the list  
count =0
for word in list_of_word:
    for character in word:
        if  character.islower():    #  check the which litter is lower case 
            count=count + 1         #  if letter is lower case then count is increase
print(count)