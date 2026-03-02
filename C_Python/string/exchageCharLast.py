text = input("Enter the string:")

result = text[-1] + text[1:-1] + text[0]

print("exchange the last character with the first character:",result)


# other way

text2 = input("Enter the string :")
new_string =""

for i in range(1,len(text2)-1):
    new_string += text[i]
new_string = text2[-1] + new_string + text2[0]
