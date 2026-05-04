# Write a Python program to drop empty elements(None) from a given dictionary

dict = {
    "name" : "navaj",
    "age"  :None,
    "color": "",
    "marks":[],
}

for only_value_key in dict:    # this code find the only key value pairs 
    if dict[only_value_key]:
        print(only_value_key,":",dict[only_value_key])
        # print(dict.keys())

print("\n")

for only_key in dict:   # this code key with empty value 
    if not dict[only_key]:
        print(only_key,":",dict[only_key])