# Write a Python program to drop empty elements(None) from a given dictionary

dict = {
    "name" : "navaj",
    "age"  :None,
    "color": "",
    "marks":[],
}

key_with_value = {}
empty_key = {}

for only_value_key in dict:    # this code find the only key value pairs 
    if dict[only_value_key]:   # this condition means take the key-value pairs because without value pairs are does not exits so
        # print(only_value_key,":",dict[only_value_key])
        key_with_value[only_value_key]=dict[only_value_key]
    else:
        empty_key[only_value_key] = dict[only_value_key]   # store the empty key
print("key value pair is :",key_with_value)
print("empty keys is :",empty_key)

# print("\n")

# for only_key in dict:   # this code key with empty value 
#     if not dict[only_key]:
#         print(only_key,":",dict[only_key])