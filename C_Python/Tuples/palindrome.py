# check the palindrome using two pointer 

tup=(1,2,3,4,5,4,3,0,1)
left =0
right = len(tup)-1

palindrome  = True
while left <= right:
    if tup[left] != tup[right]:
        palindrome =0
        print("given tuples are not palindrome:")
        break
    left+=1
    right-=1
if palindrome:
    print("given tuples are  palindrome:")
            