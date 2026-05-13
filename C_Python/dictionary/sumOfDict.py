# Write a Python program to sum all the items in a dictionary

student_marks ={
    "navaj" : 56,
    "Mujir" : 97,
    "Imran" : 78,
    "Mahi"  : 90,
    
}

print("Sum of the marks of the student is ",sum(student_marks.values()))   # using the function of sum and calculate the sum 

sum_marks = 0
for value in student_marks.values():   # using the for and take the one by one value add the variable
    sum_marks= sum_marks + value
print("marks of student is :",sum_marks)