# Write a Python program to verify that all values in a dictionary are the same
# {'a’: 12, ‘b': 12, ‘c’: 12} Check all are 12 in the dictionary. True False/


dict = {'a':1,'b':1,'c':3,'d':1}

for value in dict.values():
    if value == 1:
        print(True)
    else:
        print(False)    