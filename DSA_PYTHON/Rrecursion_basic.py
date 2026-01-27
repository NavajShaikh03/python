def printNumbers(i, n):
    # base case
    if i> n:
        return
    #recursive case
    print(i,end=' ')
    printNumbers(i+1,n)
    print(i,end=' ') 
    
printNumbers(1,5)

def fact(n):
    if n ==0:
        return 1
    return n * fact(n-1)
print(fact(5))

def isPower0fTwo(self,n:int) -> bool:
    if n <= 0:
        return False
    if n ==1:
        return True
    if n % 2!=0:
        return False
    return self.isPower0fTwo(n//2)

# gcd

def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)
#print(gcd(48,18))
def lcm(a,b):
    return (a*b //gcd(a,b))
print(lcm(4,6))
print(gcd(48,18))

class Solution:
    def findPow(self,x,n):
        #base case
        if n ==0:
            return 1
        #recursive case
        a =  self.findPow(x,n//2)
        
        if n % 2 ==0:
            return a * a
        else:
            return a*a*x
    def myPow(self,x:float,n:int) ->float:
        if n >= 0:
            return self.findPow(x,n)
            
        