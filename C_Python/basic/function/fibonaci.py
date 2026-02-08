def fibonaci():
    a,b=0,1
    n = int(input("Enter n th no. for series:"))
    print("Fibonacci series:")
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
fibonaci()
