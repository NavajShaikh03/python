text = input("Enter the string :")

seen = set()   # not store the duplicate the value
first_repeat = None

for ch in text:
    if ch in seen:
        first_repeat = ch
        break
    else:
        seen.add(ch)
    
if first_repeat:
    print("repeat character:",first_repeat)
else:
    print("no repeat character")
    
text = input("Enter a string:")

for i in range(len(text)):
    for j in range(i + 1,len(text)):
        if text[i] == text[j]:
            print("repeated ch :",text[i])
            exit()
print("no repeated character found")