# 36. Input 1o numbers using arbitrary parameters and find out occurrences of particular 
# element in from list

def count_occurrences(*numbers):
    count = 0
    x= int(input("Enter the number to find the same no. :"))
    for i in numbers:
        if i == x:
            count += 1
    print("same is present in at times : ",count)
num = [1,2,3,4,5,6,7,8,9,10,10,10]
count_occurrences(*num)
            
            
# other method
def count_occurrences(*numbers):
    s = int(input("Enter the number to find the same no. :"))
    count1 = numbers.count(s)
    print("same is present in at times : ",count1)
n  =  [1,2,1,3,2,45,32,23,53,22,43,32,24,32,34,]
count_occurrences(*n)      