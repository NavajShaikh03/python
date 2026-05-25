# . Write a Python program to find the key of the maximum value in a dictionary


dict = {
    "value1" : 34,
    "value2" : 74,
    "value3" : 84,
    "value5" : 94,
    "value6" : 354,
    "value7" : 343,
}
print(max(dict.items()))

max_value = 0
min_value = dict["value1"]
for key in dict:
    if max_value < dict[key]:
        max_value = dict[key]
    elif(min_value > dict[key] ):
        min_value = dict[key]
print("max values in  dictionary of key-pairs : ",max_value)
print("minimum values in dictionary is :",min_value)