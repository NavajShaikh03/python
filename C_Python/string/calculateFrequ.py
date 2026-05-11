text = input("Enter the string:")

visited = ""   # store the character which is already visited 

for ch in text:
    if ch not in visited:
        count =0 
        for v in text:           # take the one character and compare the first character 
            if  ch ==v:          #compare the character and count
                count +=1
            visited +=ch
        print(ch,"=",count)
    