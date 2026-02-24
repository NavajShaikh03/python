text = input("Enter the text:")
max_count = 0
max_char = ""
for char in text:
    count = text.count(char)
    if count > max_count:
        max_count = count
        max_char = char
print(f"The character that appears most frequently is '{max_char}' with a count of {max_count}.")
