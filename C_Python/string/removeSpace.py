text = input("Enter the string:")

result =""

for ch in text:
    if ch != " ":
        result+=ch
print("output:",result)

# onther method
text2  = input("Enter the string:")
result = text2.replace(" ","")
print(result)