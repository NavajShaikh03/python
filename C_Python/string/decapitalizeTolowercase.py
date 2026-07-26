# convert first letter of string into if first latter is lowercase convert into uppercase otherwise convert into lowercase

text3 = input("Enter the string:")
if text3 !="":
    first = text3[0]
    
    if 'A' <= first <= 'Z':
        first = chr(ord(first)+32)   # Convert uppercase to lowercase using ASCII values and chr() function , ord() function returns the ASCII value of a character.
    elif ('a' <= first <= 'z'):
        first = chr(ord(first)-32)   # 
    result = first + text3[1:]       # using slicing add the remaining string starting from the second character of string and first character are maked as uppercase latter 
    print("Decapitallized String:", result)