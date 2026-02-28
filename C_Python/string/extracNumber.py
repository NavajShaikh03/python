text = input("Enter the String:")

numbers =""

for n in text:
    if "0" <= n <= "9":
        numbers += n
print("Numbers in the string:", numbers)


# other method

text2 = input("Enter the String:")

numbers2 =""

for n in text:
    if n.isdigit():
        numbers2 += n
print("Numbers in the string (method 2):", numbers2)


# other method

text3 = input("Enter the String:")

numbers3 = []
temp = ""

for ch in text:
    if ch >= '0' and ch <= '9':
        temp = temp + ch
    else:
        if temp != "":
            numbers3.append(temp)
            temp = ""
            
# Add the last number if exits
if temp != "":
    numbers3.append(temp)
print("Extracted numbers :",numbers3)
        