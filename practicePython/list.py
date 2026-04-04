marks = [55,56,35,76,98,34,45,46,86,45,45,45]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-1])
print(marks[len(marks)-3])   # positive

if 66 in marks:
    print("Yes")
else:
    print("false")
    
# Same thing applies for string as well
# method

marks.append(345)
marks.sort()
marks.reverse()
print(marks.index(45))
print(marks.count(45))
print(marks)

c = marks.copy()
c[0] = 444
print(c)
c.insert(4,4444)
print(c)

m = [900,1000,1100]
marks.extend(m)
print(marks)