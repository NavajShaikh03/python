text = input("Enter the specific word or repeated:")

words = text.split()

unique_words = set(words)
result = " ".join(unique_words)
print("String after removing duplicate words:", result)


# other method 

text2 = input("Enter the String:")
words2 = text2.split()
unique_words2 = []

for word in words2:
    if word not in unique_words2:
        unique_words2.append(word)
result2 = " ".join(unique_words2)
print("String after removing duplicate words (method 2):", result2)