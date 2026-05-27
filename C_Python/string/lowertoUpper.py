
str = input("Enter the string :")

new_string = ""
for i in str:
    if i.islower():
        u = i.upper()
        new_string = new_string + u
    else:
        l = i.lower()
        new_string = new_string + l
print(new_string)