n = int(input("Enter the number for amstrom:"))
sum =0
while n > 0:
    cube_number = n % 10
    sum = sum + cube_number**3
    n = n // 10
if (n == sum):
    print(f"{sum} is not amrstrom")
else:
    print(f"{sum} is armstrom")
    
    
    