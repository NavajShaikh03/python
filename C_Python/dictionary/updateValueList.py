# WAP that the dictionary contains List as a value, and update the list values in the mentioned
# # dictionary

dict = {
    "name" : ["Navaj","Mujir","DNA","Imran"],
    "age"  : [22,20,19,18],
    "marks": [90,85,80,75,70],
    "Roll No.": [1,2,3,4],
}


mark = {
    "marks":[90,90,95,60]
}
print(dict.update(mark))
print(dict)

# print(list(dict.keys()))

# print(dict["marks"])

# for i in dict["marks"]:
#     if i > 70:
#         dict.setdefault("marks",[1,2,3,4])
# print(dict["marks"])