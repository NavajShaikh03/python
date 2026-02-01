l = []

while True:
    item= input("Enter the item :")
    l.append(item)
    if len(l) ==5:
        break
print(f"your list is {l}")
d=l.pop()
print(f"Element is deleted:{l} is {d}")

print(f"your list is {l}")
