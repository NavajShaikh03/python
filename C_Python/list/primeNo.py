# 29. Display prime numbers within specified range using list comprehension
# nums = [1,2,3,4,68,8,9,8,95,43]
# primes = [n for n in nums if n > 1 and len([i for i in range(2, n) if n % i == 0]) == 0]
# print(primes)
n=3
check = len([i for i in range(2, n) if n % i == 0]) == 0   # check the condition number are prime or not if true its prime otherwise not prime
print(check)                                               