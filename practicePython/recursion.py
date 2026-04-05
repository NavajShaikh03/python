def fact(n):
    if (n==0  or n ==1):
        return 1
    else:
        return n * fact(n-1)
result = fact(3)
print(result)
    
# 3 * fact(2)
# 3 * 2 * fact(1)
# 3 * 2 * 1 
# return value

# Fibonacci sequence

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n =6+1
sum_fibonacci =0
for i in range(n):
    print(fibonacci(i))
    sum_fibonacci = sum_fibonacci + fibonacci(i)
print(f"sum of fibonacci series of number is {n} : ", sum_fibonacci)