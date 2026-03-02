text = input("Enter the string:")

result = 0
other_string =""
for ch in text:
    result += 1
if result < 2:
    print("String is empty")
    
else:
    other_string = text[:2] + text[-2:]   # if the string length is less than 2 then return empty string otherwise return the string made of the first 2 and the last 2 chars of the original string.
    print("other string is:",other_string) # make the string made of the first 2 and the last 2 chars of the original string.
    