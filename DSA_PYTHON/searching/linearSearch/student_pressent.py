'''
Teacher checks if a student is pressent by reading names from an attendce sheet.
check names are not awlays sorted 
one by one checking is natural
dataset is small
'''

def is_student_present(arr, name):
    for i in range(len(arr)):
        if arr[i] == name:
            print("Student is present")
            return True                  #  stope the loop and return True
    print("Student is not present")
    return False    
students = ["alice","bob","charlie","david"]
name = "charlie"
is_student_present(students,name)
name = "eve"
is_student_present(students,name)