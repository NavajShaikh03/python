# 14. Write a Python program to get the maximum and minimum values of a dictionary.

marks = {
    "navaj" : 89,
    "mujir" : 88,
    "Imran" : 77,
    "mahi"  : 98,
    "Rahul" : 90,
    "Vaibhav": 56,
}

print("minimum marks of student is ",min(marks.items()))
print("Maximum marks of student is :",max(marks.items()))

max_marks = 0
min_marks = 0

for mark_key in marks.keys():   # this loop reach to end 
    if marks[mark_key] > max_marks:
        max_marks = marks[mark_key]
    else:
        min_marks = marks[mark_key]
print(f"max marks is {max_marks} and minimum marks is {min_marks}")
        