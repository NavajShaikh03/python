# tuple cannot change but like the same the list

tup = (1,3,5,6)
print(type(tup))

tup = (1,2,3,4,5,7,9,0,"45",345,"green")
print(tup)
print(tup[0])
print(tup[2])
print(tup[-1])
print(tup[:])
print(tup[1:4])
if 234 in tup:
    print("yes present")
    
# method

countries = ("Spain","Italy","India","England","Germany")

temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)            # remove
temp[2] = "Finland"    # change item
countries = tuple(temp)
print(countries)
c = countries.count("Italy")
print(c)

c = countries.index("Italy")
print(c)
print(len(countries))

# marge tuple 
countries1 = ("Pakistan","Afghanistan","Bangladesh","ShriLanaka")
countries2 = ("Vietman","India","China")
sountEastAsia = countries1 + countries2
print(sountEastAsia)