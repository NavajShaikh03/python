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
        filtered[key] = value
    else:
        felled[key]=value
print("Passed student is :",filtered)
print("Felled Student is :",felled)