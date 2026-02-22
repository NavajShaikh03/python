"""
Algorithm for merge sort 
1.start 
2 if list has 0 or 1 element  then 
3.
4.apply merge sort on left half
5.apply merge sort on right half
6.merge two sorted halves into sorted list 
"""

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])
    
    return merge(left,right)
def merge(left, right):
    result =[]
    i=j=0
        
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
        
arr = [22,3,34,53,35,65,64,2,7,45,13]
print(merge_sort(arr))



# q