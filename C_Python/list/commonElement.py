first_list = [1,2,3,4,5,6,7,8,9]
second_list = [1,4,2,5,6,92,54,3]

common_element = []

for i in first_list:
    if i in second_list:
        common_element.append(i)
print("common element in both list:",common_element)


# other way to find common element in both list using set data structure

third_list = first_list + second_list    #   combine the two list then 
print("third list:",third_list)

common_element_set = set()

print("common element:",set(third_list))
