number =  [12,23,45,67,78,89]
print( "your list is:",number)
n=len(number)-1
print(n)

key = int(input("Enter the check present or not in list:"))
while n>=0:
    if number[n] == key:
        print(f"your number are present in list at index number:{n}")
        return
    else:
        print("no. not found")
        break
    n-=1
        