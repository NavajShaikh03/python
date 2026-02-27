text = input("Enter the specific word:")

text_to_word = text.split()

large_word =text_to_word[0]
small_word =text_to_word[0]

for word in text_to_word :
    if len(word) > len(large_word):
        large_word = word
    if len(word ) < len(small_word):
        small_word = word

print(large_word)
print(small_word)

# onther method using the built in function

text2 = input("Enter the specific word:")

text_to_word2 = text2.split()

smallest = min(text_to_word2,key=len)
largest = max(text_to_word2,key=len)

print("Smallest",smallest)
print("largest",largest)