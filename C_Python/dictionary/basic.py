# concept of dictionary

# Dictionary stores data in key : value format
# It is mutable (can add, update, delete)
# Keys are unique (no duplicates allowed)
# Values can be any data type
# Keys must be immutable (string, int, tuple)
# Access values using key → dict["key"]
# Provides fast data lookup
# Common methods: keys(), values(), items()

# student.keys()     # get all keys
# student.values()   # get all values
# student.items()    # get key-value pairs

# method if dictionary is

# keys() → returns all keys
# values() → returns all values
# items() → returns key–value pairs
# get(key) → returns value (safe, no error if key not found)
# update() → adds or updates multiple items
# pop(key) → removes specific key            ->
# popitem() → removes last inserted item
# clear() → removes all items
# copy() → creates a copy of dictionary
# # setdefault(key, value) → returns value, adds key if not present

dic = {
    "name" :"navaj",
    "age"  :22,
    "color":"red",
    "other_color":"Black_and_white",
}

print(dic.items())   # give the all pairs of keys and values
print(dic.keys())    # give the all keys of dictionary
print(dic.values())  # give the all value of keys present in dictionary  

take_key = dic.get("age")  # give the key if key are not found then return none 
print(take_key)

other_dic = {
    "name" : "Mujir",
    "age" :20,
    "color":"red",
    "village" : "Begampur",
    "my" : "hart",
}

dic.update(other_dic)   # update the dic with other_dic if keys are same then replace the keys 
print(dic)

dic.pop("name")      # remove the name keys from the dictionary 
print(dic)

dic.popitem()        # remove the last item from dictionary
print(dic)

copy_dic = dic.copy() #creat the copy of dictionary 
print(copy_dic)

dic.clear()           # remove the dictionary of all items
print(dic)

dic.setdefault("name","mahi")    # add the key in the dictionary
print(dic)
dic.setdefault("name","navaj")     # if you add key and if key are exit not replace old keys 
print(dic)

dic.fromkeys("name")     # return the pairs of name 
print(dic)