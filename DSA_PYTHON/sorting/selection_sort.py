'''
Algorithm
1.start
2.Assume that first element is small
3.compare with all other element to find true smallest
3.swap the smallest element with first element
5.move to next element and repeat the steps 
6.Continue until list is sorted
'''

def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index = i   # select as fist smallest element
        
        for j in range(i+1,n):  # this loop find the smallest value in arr
            if arr[j] < arr[min_index]:
                min_index =j
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

arr = [1,3,4,6,2,9,4,3]

s = selection_sort(arr)

print(s)

