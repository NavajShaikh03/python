#Write a Python program to create a dictionary from a string. i/p hello o/p : {‘h’:1,’e’:1,’l’:2…}


dict = {}
string = input("Enter the string:")   # Take the user input 
for chr in string:
    chr_count = string.count(chr)     # count the character of string each letter
    dict.setdefault(chr,chr_count)    # this method add the key-value pairs in empty dictionary
print(dict)