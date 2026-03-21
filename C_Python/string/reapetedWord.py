# . Implement program to find the first repeated word in a given string.
# I/P String : ab ca bc ab" O/P : ab

text = input("Enter the spefic word or reapeted word:")

words = text.split()
repeated_word = []
for word in words:
    if word in repeated_word:
        print("First Repeated Word:", word)
        break
    else:
        repeated_word.append(word)
        