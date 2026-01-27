def addition(n):
    if (n > 10):   # base case
        return 
    print(n)
    return addition(n+1)
addition(1)



def sum0fNum(n):
    if n ==0 :
        return 0
    return n+sum0fNum(n-1)
sum = sum0fNum(10)
print(f"sum is :{sum}")

def countDigits(n):
    if n == 0:
        return 0
    return 1 + countDigits(n//10 and n % 10)     
print(countDigits(12345))




def sumDigits(n):
    if n == 0:
        return 0
    return n%10 + sumDigits(n//10)     
print(countDigits(12345))

# factorial 

def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# fibonaci

def f(n):
    if n<=0 :
        return 0
    if n==1:
        return 1
    return f(n-1) + f(n-2)
for i in range(10):
    print(f(i),end=' ')

# a investor strategy
#  first month 1 $ invest
#  second  month 1 $ invest
#  from the third month onward the monthly investment equals the sum of the investment of the previous two month

# def f(n):
#     if n ==1 or n==2:
#         return 1
#     return f(n-1) + f(n-2)

# def t_invest(n):
#     if n ==0:
#         return 0
#     return sum(f(i) for i in range(1,n+1))
# print(t_invest(5))




print("\n")

# calculate the size of a folder using recursion
def folder_size(path):
    import os
    total_size =0
    for entry in os.scandir(path):
        if entry.is_file():
            total_size += entry.stat().st_size
        elif entry.is_dir():
            total_size += folder_size(entry.path)   # recursive call
    return total_size
folder_path ="D:\\Downloads\\STOCK-DASHBORD (1)"
size = folder_size(folder_path)
print(f"Total size of folder '{folder_path}' is {size} bytes")
            
            
cart = [
    {"type":"item","price":1},
    {"type":"item","price":1},
    {
        "type":"bundle",
        "items":[
            {"type":"item","price":1},
            {"type":"item","price":1},
            {
                "type":"bundle",
                "items":[
                    {"type":"item","price":1},
                    {"type":"item","price":1},
                    {
                        "type":"bundle",
                        "items":[
                            {"type":"item","price":1},
                            {"type":"item","price":1}
                        ]
                    }
                ]
            }
        ]
    }
]

def cartTotal(cart):
    total =0
    
    for element in cart:
        if element["type"] == "item":
            total+= element["price"]
        elif element["type"] == "bundle":
            total += cartTotal(element["items"])   # recursive call
    return total
total_price = cartTotal(cart)
print(f"Total price of cart is : {total_price}")

#  1 to n

