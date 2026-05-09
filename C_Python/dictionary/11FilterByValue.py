# WAP to filter a dictionary based on values

# filter means check the conditions 

Student_percentage = {
    "navaj" :89,
    "Mujir" :90,
    "Imran" :78,
    "Mahi"  :98,
    "Rahul" :78,
    "Deep"  :34,
    
}

filtered = {}
felled = {}
for key , value in Student_percentage.items():
    if Student_percentage[key] >= 35:
        filtered[key] = value              # store the key-value pairs which the grater then 35 in variable 
    else:
        felled[key]=value                  # store the value less then 35 in variable...
print("Passed student is :",filtered)
print("Felled Student is :",felled)