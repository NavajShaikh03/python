# # Dictionary are ordered collection of data item.They store multiple item in single variable ,
# # Dictionary item are key-values pairs that are separated by commas and enclosed and within curly
# # brackets {}.
# dic = {
#     "name"  :"navaj",
#     "age"   :22,
#     "vilage":"Solapur",
#     "branch":"DS",
#     "CGPA"  :9.1,
#     "color" :"black",
# }
# print(dic)
# print(dic["name"])
# print(dic["age"])
# print(dic.get('name'))   #  not show the the error when not find the key return None
# # print(dic["name2"])      #   when the key are not found then get error 
# print(dic.keys())        # return the all key
# print(dic.values())


# for key in dic.keys():
#     print(f"The value corresponding to the key {key} is : {dic[key]}")
    
# print(type(dic.items()))
# for key,value in dic.items():
#     print(f"the value of corresponding to the key {key}:{value}")
    
    
# ## method of dictionary

# # employee performance
# ep1 = {
#     1:65,
#     2:35,
#     3:98,
#     4:78,
#     5:90,
#     6:89,
#     7:74,
#     8:89,
#     9:90,
#     10:78,
# }

# ep2 = {
#     11:80,
#     12:20,
#     13:30,
#     14:78,
#     15:60,
# }

# ep1.update(ep2)
# print(ep1)

# ep1.clear
# print(ep1)

# empty = {}
# print(type(empty))

# ep2.pop(12)      #  remove the key from dictionary
# print(ep2)

# ep2.popitem()   # remove the last element from list
# print(ep2)

# del ep1[15]     # delate the specific key
# print(ep1)

# del ep1 # delate the dictionary

d = {
    "name":"mujir",
    "age":45,
}
print(d)
print(d["name"])
print(d["age"])
d2 = {
    "brother_name":"imran",
    "imran_age":19,
    "color":"black",
}

d.update(d2)
print(d)

for item in d.keys():   # print the all key 
    print(item) 
    
for value in d.values():     #  print the all value from dictionary
    print(value)


for key in d.keys():
    for value in d.values():
        print(f"pairs of data is {key}:{value}")
        break
    