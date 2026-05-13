# 14. Write a Python program to get the maximum and minimum values of a dictionary.

marks = {
    "navaj" : 89,
    "mujir" : 88,
    "Imran" : 77,
    "mahi"  : 98,
    "Rahul" : 90,
    "Vaibhav": 56,
}

print("minimum marks of student is ",min(marks.values()))
print("Maximum marks of student is :",max(marks.values()))

max_marks = 0
min_marks = 0

for mark in marks.values():   # this loop reach to end 
    if mark > max_marks:
        max_marks = mark
    else:
        min_marks = mark
print(f"max marks is {max_marks} and minimum marks is {min_marks}")
        