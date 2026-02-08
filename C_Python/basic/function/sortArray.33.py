#Q34. Write a program to sort array in ascending & descending.
def sort_arrary(arr):
    # using bubble sort to sort the array in ascending order
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Array is sorted in assending order:",arr)
    # using bubble sort to sort the array in descending order
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    print("Arrary is sorted in desending order:", arr)
s =[ 4,35,26,7,78,25,67,75,38,54,67]
sort_arrary(s)                