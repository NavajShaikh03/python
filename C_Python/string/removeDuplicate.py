text = input("Enter the text:")

seen = set()
result = ""

for char in text:
    if char in seen:
        continue
    seen.add(char)
    result += char
print("String after removing duplicates:", result)
        