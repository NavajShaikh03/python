# 2. WAP to check whether a given key already exists in a dictionary

dic={
    "name" : "navaj",
    "age"  : 22,
    "village":"Solapur",
}

key_name = input("Enter the keys name :")    # take the key name from user 

if key_name in dic:
    print("keys already present in dictionary")
else:
    print("Keys are not present in dictionary can you add this keys in dictionary ")