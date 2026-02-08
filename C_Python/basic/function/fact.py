def fact(n):
    factorial =1
    for i in range(1,n):
        factorial = factorial *i
    return factorial
print(fact(5))