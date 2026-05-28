
str = input("Enter the string :")     ## take the user input as a string

new_string = ""    # after that check the character lower or upper and add the they char
for i in str:
    if i.islower():
        u = i.upper()
        new_string = new_string + u
    else:
        l = i.lower()
        new_string = new_string + l
print(new_string)