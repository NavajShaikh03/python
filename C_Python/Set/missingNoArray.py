# find the missing number using the set

#missing number without using set
arr = [0,1,2,3,4,5,6,10,10,10,11]
lst = []
count = 0
for num in range(min(arr),max(arr)+1):
    if num not in arr:
        count+=1
        lst.append(num)
print("actual arr :",arr)
print("missing element from arr:",lst)
print("count missing number of arr is: ",count)


# missing element using set 

arr = [1,3,5,7,9,]

expected = set(range(min(arr),max(arr)+1))
actual = set(arr)
missing_element =(expected - actual )  

print("\nactual arr is :",arr)
print("missing element from arr :",missing_element)
print("count of missing element is :",len(missing_element))
