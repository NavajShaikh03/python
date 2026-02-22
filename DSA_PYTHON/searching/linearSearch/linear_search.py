'''
1.start
2.start from the first element of the list/array
3.compare the target value with the current element
4.if found, return the index of the element
5.if not found, move to the next element and repeat step 3 until the end of the list/array is reached
6.if the target value is not found in the list/array, return -1
'''


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

arr=[10,20,30,40,50]
key=20
result = linear_search(arr,key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array")

