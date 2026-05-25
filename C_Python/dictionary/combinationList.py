# . Write a Python program to create and display all combinations of letters, selecting each letter 
# from a different key in a dictionary. I/P {'1':['a','b'], '2':['c','d']} O/P ac ad bc bd

dict = {
    "1" :["a","b"],
    "2" :["c","d"],
}

list_value = []
for character in dict["1"]:   #  Take one character from on list and multiply the second list of dictionary
    for value in dict["2"]:
            list_value.append(character * value)
print(list_value)