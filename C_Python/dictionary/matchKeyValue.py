# 6. WAP to match key values in two dictionaries.

dict1 = {
    "name" : "navaj",
    "age"  : 22,
    "color":"red",
}

dict2 ={
    "name" : "navaj",
    "age"  : 22,
    "color":"black",
}

for value1 in dict1.values():
    for value2 in dict2.values():
        if value1 == value2:
            print("matched values of dictionary is :",value1)

# other way to 

for item in dict1.items():   # find the keys-values pairs of both dictionary
    if item in dict2.items():   # match the same items from both dictionary and return
        print(item)
        
# other ways to find the pairs 

matched_pairs  = dict(dict1.items() &  dict2.items())    # & → used for matching/intersection 
print(matched_pairs)