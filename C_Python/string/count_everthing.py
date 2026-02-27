text = input("Enter the text:")
upper_count =0
lower_count = 0
specialChar_count =0
digit_count =0
space_count =0 

for char in text:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1
    elif char.isdigit():
        digit_count+=1
    elif char.isspace():
        space_count+=1
    else:
        specialChar_count+=1
print("count of uppercase characters is :",upper_count)
print("count of lowercase characters is :",lower_count)
print("count of digits is :",digit_count)
print("count of special characters is :",specialChar_count)
print("count of spaces is :",space_count)


# onther method using without built in function

text2 = input("Enter the text2:")

upper = lower =digit = space = specialChar = 0

for ch in text2:
    if 'A' <= ch <= 'Z':
        upper+=1
    elif 'a' <= ch <= 'z':
        lower+=1
    elif '0' <= ch <='9':
        digit+=1
    elif ch == ' ':
        space+=1
    else:
        specialChar+=1

print("count of uppercase characters is :",upper)
print("count of lowercase characters is :",lower)
print("count of digits is :",digit)
print("count of special characters is :",specialChar)
print("count of spaces is :",space)
