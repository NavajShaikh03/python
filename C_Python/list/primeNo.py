# 29. Display prime numbers within specified range using list comprehension

primes = [n for n in nums 
        if n > 1 and len([i for i in range(2, n) if n % i == 0]) == 0]
print(primes)