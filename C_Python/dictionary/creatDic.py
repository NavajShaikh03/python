# 1. WAP to concatenate the two dictionaries to create a new one    

dic1={                        # first dictionary and its content
    "name" : "navaj",
    "age"  : 22,
    "village":"Solapur",
}

dic2 ={                        # this is second dictionary
    "SirName" : "Shaikh",
    "Equcation" :"B-Tech",
    "CGPA": 9.00,
}

dic1.update(dic2)   # add the all data of dci2 in the dic1
print(dic1)