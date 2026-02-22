# Algoritham of buble sort


# start
# start the from first element
# compare next element if greater then swap otherwise move nex element same steps reapate 


# bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-1-i):  #  n-1-i not gate the sorted element
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [5,4,3,2,1]
print(print(bubble_sort(arr)))

# in the class student are standing in a line randamly by hight a teacher want thay to stand assending order only addjust student compare cif lenght toler right stident this prosece     
    
    
def student_list(l):
    student_length = len(l)
    
    for i in range(student_length):
        for j in range(0,student_length-1-i):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            else:
                break
    return student_list

l = [1.2,3.1,4.1,3.2]
print(print(student_list(l)))                
        
        
        
        
def orders_prep(orders):
    n =len(orders)
    
    for i in range(n):
        for j in range(0,n-1-i):
            if orders[j][1] > orders[j+1][1]:
                orders[j],orders[j+1] = orders[j+1],orders[j]
    return orders

orders =[("A",4),("B",1),("C",3)]

print(orders_prep(orders))