'''
start
set low = and high = n-1 





ex:
1 2 4 5 6 7 8 9

'''


def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid  = (low + high) // 2
        
        if arr[mid] == key:
            return mid 
        
        elif arr[mid] < key:
            low = mid - 1
        else:
            high = mid + 1
    return -1

arr =[1,2,4,5,6,7,8,9]

key = 5
result = binary_search(arr,key)

if result != -1:
    print("Element found at index;",result)
else:
    print("Element not found in the array")
    
    