name = str(input("Enter the Student Name:"))
marks = list(int(input("Enter the 5 subject marks:")))
for i in marks:
    sum=sum + i
    

percentage = sum/5

if (percentage >=0 and percentage < 35):
    if(percentage == 0):
        print("Invalid percentage{percentage}")
    else:        
        print(f"{name} is Fail")
elif(percentage >=35 and percentage <=50):
    print("Grade is C of Student {name}")
elif(percentage > 50 and percentage <= 75):
    print("Grade is B of student {name}")
elif(percentage >75 and percentage <= 90 ):
    print("grade is A of Student {name}")
else:
    if(percentage == 100):
        print("Check again your percentage ")
    else:
        print("Grade is A+")    