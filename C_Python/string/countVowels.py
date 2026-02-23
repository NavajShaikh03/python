text = input("Enter the text:")

vowels = "aeiouAEIOU"
count = 0
found_vowels = []

for char in text:
    if char in vowels:
        count+=1
        found_vowels.append(char)
print("vowels in text:",found_vowels)
print("count of vowels is:",count)