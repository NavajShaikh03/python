# tup = (34,345,234,23,2356,848,94940,94)
# sorted_tup=(sorted(tup))
# print("second largest element in tuples :",sorted_tup[-2])

#  other method 
tup = (353,32,353,13,531,135,433,252,234,532,123,433)
lst = list(tup)    # convert the tup to list because tuple is immutable 
for i in range(0,len(lst)):
    for j in range(1+i,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j] = lst[j], lst[i]
print(lst)
print("second largest number :",lst[-2])
print("second minimum number :",lst[1])