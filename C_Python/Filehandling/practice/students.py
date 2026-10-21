with open("D:\python\C_Python\Filehandling\practice\studensts.txt","r") as f:
    # data = f.read() # first you can user this then use for loop not print something else because curser reached at the end 
    
    for line in f:
        print(repr(line))   # repr function print what acuty in the string of in each line and at the end curser reached the end 
    
    f.seek(0)
    
    # i want find the height marks
    
    height_name = ""
    height_marks = 0
            
    for line in f:
        name,marks = line.strip().split(",")
        print(name,marks)
        marks = int(marks)
    
        if marks > height_marks:
            height_marks =marks
            height_name = name
    print("high marks with high  name: ",height_name)
    print("high marks with high marks: ",height_marks)
            
    # i want to calculate the average marks
        
            
        


        
    
    # i want find the height marks 
    
    