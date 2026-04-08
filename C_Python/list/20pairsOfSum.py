lst = [4,2,6,7,8,7,9,6,2,5,7]
pairsList = []

for i in range(0,len(lst)):
    for j in range(0 ,len(lst)):
        pair =(lst[i] + lst[j])
        if  (lst[i] + lst[j]) == 13:
            if [lst[i],lst[j]] not in pairsList:
                # pairsList = pairsList + [lst[i],lst[j]]
                # print(pairsList)
                print(lst[i],lst[j])
                