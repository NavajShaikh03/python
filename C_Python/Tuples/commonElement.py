tup1 = (34,343,23,23,56,98,90,78,90,67)
tup2 = (54,32,12,43,66,76,55,86,44,77,98,90)

lst = []
for common in tup1 :
    if common in tup2 and common not in lst : # count the number once if reapited number not consider
            lst.append(common)
            print("common element from both tuples:",common)
print("common element :",lst)