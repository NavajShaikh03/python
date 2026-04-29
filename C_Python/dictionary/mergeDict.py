# marge the dictionary 

dic1 = {
    "name"   : "navaj",
    "age"    : 22,
    "village": "Begampur",
    "marks"  : 9.1,
}

# Second dictionary is 

dic2={
    "name" : "Mujir",
    "age"  : 20,
    "city" : "Kolhapur",
    "marks": 8.5,
}

# dic1.update(dic2)    # change the all data of dictionary 1 
# print(dic1)


# for key in dic2.keys():
#     for value in dic2.values():
#         print(key,value)


# other way 
merged = {}     # empty dictionary
for key in dic1: # dictionary 1 add in merged 
        if key in dic2:
            merged[key] = [dic1[key],dic2[key]]
        else:
            merged[key]=dic1[key]

for key in dic2:     # dictionary 2 add in merged 
    if key not in merged:
        merged[key] = dic2[key]

print(merged)