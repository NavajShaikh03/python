def number(num):
    n = len(num)
    for i in range(n):
        for j in range(0,n-1-i):
            if num[j] > num[j+1]:
                num[j] , num[j+1] = num[j+1],num[j]
    return num

num = [12/13 , 7/6 ,19/17, 16/18, 21/29, 34/43, 27/24, 7/13]

sort = (number(num))

print(sort)

def number(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-1-i):
            a, b = map(int, num[j].split('/'))
            c, d = map(int, num[j+1].split('/'))

            if a/b > c/d:
                num[j], num[j+1] = num[j+1], num[j]
    return num

num = ["12/13", "7/6", "19/17", "16/18", "21/29", "34/43", "27/24", "7/13"]

print(number(num))
