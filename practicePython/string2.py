# STRING 

name = "!!!harry"
friend = "Rohan"

anotherFriend = 'Lovish'
apple = ''' He said , hi harry, 
hey i am good 
I want to eat apple'''

print("hello,+ ", name)

print(name[0:-2])

print(name.upper())
print(name.lower())
print(name.replace('Harry','navaj'))
print(name.split(" "))
print(name.capitalize())

str1 = "welcome to the Console "

print(len(str1))
print(str1.center(100))
print(str1.endswith("to",4, 10))

str1 = "He name is Dan. He is an honest man."
print(str1.find("Dan"))
print(str1.index("is"))   # find the index no. of specific word and character in the string  
str2 = "WelcomeToTheConsole"
print(str2.isalnum())   # is the check the string inquild in sring of (a-z,A-Z,0-9) in string yes then print True 

print(str2.isalpha())  # check the string which the alpha or not 

print(str2.islower())   # check the string lower or not 

str3 = "We wish you a Merry Christmas\n"
print(str3)
print(str3.isprintable())  # which character is printable in string check the 


str4 = "            "
print(str4.isspace())   # space is present in string then return true

str5 = "World health organization"
print(str5.istitle())

str6 = "Python is the a Interpreted language"
print(str6.startswith("Python"))

print(str6.swapcase())   # convert into upper case and upper case into lower

str7 = "His name is Dan. Dan is an honest man."
print(str7.title())        # this convert in title form 