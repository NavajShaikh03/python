# . Implement program that accepts a comma-separated sequence of words as input and prints 
# the distinct words in sorted form (alphanumerically).
# I/P String : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

text = input("Enter the words with comma separated:")

words = text.split(",")
print(words)

result = sorted(set(word.strip() for word in words))   # when line execite then become the list of words and then remove the duplicate word and then sort the word in alphanumerically order
new_string= ", ".join(result)  # this line is used to join the word with comma and space
print(result)
print(new_string)


# other way

text2 = input("Enter the words with comma separted :")

# split the word using comma
words2 =text2.split(",")

clean_words=[]

# manualliy remove the space from beginning and end

for word in words2:
    
    # remove the space from beginning and end
    start =0
    while start < len(word) and word[start] == " ":
        start +=1
        
    # remove the space from end
    end = len(word)-1 
    while end >=0 and word[end] ==" ":
        end -=1
        
    cleaned = word[start:end+1]  # this line is used to get the cleaned word without space
    clean_words.append(cleaned) # this line is used to add the cleaned word in the list 

# remove the duplicate word using set and then sort the word 
unique_words = []
for wor in clean_words:
    if word not in unique_words:
        unique_words.append(word)
        
# sort the word in alphanumerically order

for i in range(len(unique_words)):
    for j in range(i+1, len(unique_words)):
        if unique_words[i] > unique_words[j]:
            unique_words[i] ,unique_words[j] = unique_words[j], unique_words[i]
print(unique_words)
