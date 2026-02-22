'''
Algorithm 

1.start
2.Start from second element (index 1) 
3.Sorted  the current value
4.Compare with all other element
5.shift all element to the right greater then the value 
6.insert the value to the correct position 
7.Repeat the steps until element sorted
 
'''


def insertion_sort(arr):
    for i  in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        print(arr)
        arr[j+1]=key
        print(arr)
    return arr
num =[7,3,9,1]
i =insertion_sort(num)
print(i)

# youare teacher and you has student marks list you want display marks in assending you are easily find top student and the lowest scores 
#since the class size  is small less then  20 st. you decide to use the insertion sort marks[56,67,34,67,89,98]
  
def insertion_sort(marks):
    for i  in range(1, len(marks)):
        key = marks[i]
        j = i-1
        
        while j >= 0 and marks[j] < key:
            marks[j+1] = marks[j]
            j-=1
        marks[j+1]=key
        print(marks)
    return marks
marks=[56,67,34,67,89,98]
i =insertion_sort(marks)
print(f"\nlist of student:{i}")


# you ar book manager and you have book price you want range book s in assending order si that customer find chifest and most expensive 

# def insertion_sort(marks):
#     for i  in range(1, len(marks)):
#         key = marks[i]
#         j = i-1
        
#         while j >= 0 and books[j] < key:
#             books[j+1] = books[j]
#             j-=1
#         books[j+1]=key
#         print(books)
#     return books
# books=[2300,4500,7000,1000,15000]
# i =insertion_sort(marks)
# print(f"\nbooks price :{i}")


# you are managing tickit counter at movie thether people arrive stand in queue but vip customer later and must move be foreword best level of name , tick no. vip level 1-5 you need solve q so that higher privorty come fist but maintain the relative order of poeple with the same vip level
# queue =[("Nehal,101,2"),("Pushkar,102,5"),("Ayush,103,1")]

def vip_customer(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-1-i):  #  n-1-i not gate the sorted element
            if arr[j][2] < arr[j+1][2]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [("Nehal",101,2),("Pushkar",102,5),("Ayush",103,1)]
(print(vip_customer(arr)))