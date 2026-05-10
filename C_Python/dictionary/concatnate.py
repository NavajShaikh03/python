# Write a Python script to concatenate the following dictionaries to create a new one

# concatenate mean combine the dictionary

dict1 ={
    "name" : "navaj",
    "class": "B-tech",
    "Div"  : "A",
    "color":"black",
    
}

dict2 = {
    "name" : "Pushkar",
    "class":"B-Tech",
    "Div"  : "A",
    "age"  :23,
    
}


 
# d1 = {"a": 1}
# d2 = {"b": 2}
# d3 = d1 | d2   # this symbol used the combine the dictionary but work python version greeter then 3.9+
# print(d3)

new_dict = {}
for key2 in dict2:   # this for loop take the key from the dict2
    
    if key2 not in dict1:  # this condition check the key present in the second dictionary or not
        new_dict[key2] = dict2[key2]
        
    for key in dict1:
        if key in dict2:
            new_dict[key] = [dict1[key],dict2[key]]
        else:
            new_dict[key]=dict1[key]
print(new_dict)