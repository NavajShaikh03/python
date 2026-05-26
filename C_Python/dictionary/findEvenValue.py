# Write a Python program to find the key of the even value and should be greater than 25 in 
# a dictionary

dict = {
    "Mujir" : 34,
    "Navaj" : 23,
    "Mahi"  : 21,
    "Imran" : 20,
}

for key in dict.keys():
    if dict[key] > 25:
        print(key ,":",dict[key])