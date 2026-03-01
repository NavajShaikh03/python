text = input("Enter the string:")

result =""

for ch in text:  # remove the space in the string
    if ch != " ":
        result+=ch
print("output:",result)

# other method
text2  = input("Enter the string:")
result = text2.replace(" ","")
print(result)