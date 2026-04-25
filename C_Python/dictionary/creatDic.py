# 1. WAP to concatenate the two dictionaries to create a new one    

dic1={
    "name" : "navaj",
    "age"  : 22,
    "village":"Solapur",
}

dic2 ={
    "SirName" : "Shaikh",
    "Equcation" :"B-Tech",
    "CGPA": 9.00,
}

dic1.update(dic2)   # add the all data of dci2 in the dic1
print(dic1)