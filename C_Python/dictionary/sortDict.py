# Write a Python program to sort a list alphabetically in a dictionary


dict = {
    "name" : "navaj",
    "age"  : 22,
    "color": "red",
    
}

print(sorted(dict))              # this print only key in assending order by default using key 
                                # sorted is create a new dictionary and .sort change in the original list 
print(sorted(dict.items()))      # arrange the using keys 

 
dict_list = {                       # keys list 
    "fruits": ["banana","Apple","mango"],   
    "color" : ["red","blue","black","origen"],
}
key_sorted = sorted(dict_list.items())
print(key_sorted)

for key in dict_list:
    dict_list[key].sort()
    dict_list[key].index()
    print("count of the key if list:",dict_list[key].count())
print((dict_list))


for index in dict_list[key]:
    index.index("index")
    
    