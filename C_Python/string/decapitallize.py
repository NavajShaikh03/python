
# Decapitallize the first letter of a string
text  = input("Enter the String:")

if text !="":
    result = text[0].lower() + text[1:]
    first = text[0]
    
    if 'A' <= first <= 'Z':
        first = chr(ord(first)+32)   # Convert uppercase to lowercase using ASCII values and chr() function , ord() function returns the ASCII value of a character.
    result = first + text[1:]
    print("Decapitallized String:", result)
    
    

# other way to slove

text2 = input("Enter the String:")

if text2 !="":
    first = text2[0]
    
    if 'A' <= first <= 'Z':
        first = chr(ord(first)+32)   # Convert uppercase to lowercase using ASCII values and chr() function , ord() function returns the ASCII value of a character.
    result = first + text2[1:]
    print("Decapitallized String:", result)
    
# other way to slove
text3 = input("Enter the string:")
if text3 !="":
    first = text3[0]
    
    if 'A' <= first <= 'Z':
        first = chr(ord(first)+32)   # Convert uppercase to lowercase using ASCII values and chr() function , ord() function returns the ASCII value of a character.
    result = first + text3[1:]
    print("Decapitallized String:", result)