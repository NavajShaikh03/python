str1 = input("Enter the first string:")
str2 = input("Enter the second string:")

common =""
for char in str1:
    if char in str2 and char not in common:
        common+=char
print("common characters are: ",common)