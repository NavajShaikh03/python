text = input("Enter the string:")

word = text.split()
repeat = []
for i  in word:
    count =0
    for j in word:
        if i ==j and i not in repeat:
            count +=1
    if i not in repeat:
        repeat.append(i)
        print("the count of word",i,"is:",count)
