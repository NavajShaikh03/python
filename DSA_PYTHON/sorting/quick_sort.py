'''
Quick Sort Algorithm Implementation in Python

1.start
2.choose a pivot element (first , last or middle)
3.partition the array:
    a.small element on left side of pivot 
    b.move larger element on right side of pivot
4.Recursively the steps:
     4.1 left sub-array
        4.2 right sub-array
5 stop sub array size <=1
'''


def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [23,34,3,37,8,0,1,67,88]
q=quick_sort(arr)
print(q)


# a online platform store  display ing product the suste must be sort prise to lowest to hight a customer easily find the
# afordalbe product use appropriat sorting taken can be large (dta set ) so quick sort is best suited for this



def quick_sort(arr):
    if len(arr) <=1:   #check the list size 
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [23,34,3,37,8,0,1,67,88]
q=quick_sort(arr)
print(q)

#  a company store  employee salary sorting to genreate report and analysis pay role the hr need to sort the emp salary data from lowest to highest
# hr ststyme emp( name  salary and status ) sytem must consider only active emp ignore salary belove theshhold sort the by salary in assending order 
# emp must be active salary >30000  ex emp_data=[('emp1',45000,'active')


def quick_sort(emp):
    if len(emp) <=1:   #check the list size 
        return emp
    
    pivot = emp[0][1]
    left = []
    right = []
    
    for emp in arr[1:]:
        if emp[i] <= pivot[1]:
            left.append(emp)
        else:
            right.append(emp)
    return quick_sort(left) + [pivot] + quick_sort(right)

emp = [('emp1',45000,'active'),('emp2',25000,'inactive'),('emp3',60000,'inactive'),('emp4',15000,'active')]
filter_emp =[]
for emp in emp:
    name, salary, status = emp
    if status == 'active' and salary > 30000:
        filter_emp.append(emp)

new_emp=quick_sort(filter_emp)
print(new_emp)

