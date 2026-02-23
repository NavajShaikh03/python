inputString = "abc.pqr,xyz"
inputString = inputString.replace(".",",")
print(inputString)

# onther method

text = "abc.pqr,xyz"

result =""

for ch in text :
    if ch == ".":
        result+=","
    else:
        result+=ch
print(result)
    