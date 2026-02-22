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
            
        
        
        
        
def steps(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    print(n,end =" ")
    return steps(n-1)
steps(10)

# a book has n pages write reacursive function to count pages from 1 to n so if you enter 5 like output 1 3 4 5

def pages_count(current ,n):
    if current > n:
        return 
    print(current)
    return pages_count(current + 1, n)

pages_count(0,10)

# a city map represented as tree where each junction lead to other junction write recursive fun to count the total numbers of rechable junction from a give start point
 

# map = {
#     "A":["B","C"],
#     "B":["B","C"],
#     "C":["B","C"],
#     "D":["B","C"],
#     "E":["B","C"],
#     "F":["B","C"],
# }

# def count_junction(map,start):
#     count =0
#     for junction in map[start]:
#         count = count + count_junction(map,junction)   #recursive call when the call itself the change the start 
#     return count
# print(count_junction(map,"A"))
        
# a game has levels and sub level each level may unlock multiple sub-levels write recursive function to calculate the maximum depth of game

game_level = {
    "level 1" : ["level 1.1","level 1.2"],
    "level 1.1" : ["level 1.1.1"],
    "level 1.2" : [],
    "level 1.1.1" : ["level 1.1.1.1"],
    "level 1.1.1.1" : [],
}

def level(game_level,game):
    count =0
    for game in levelm[game_level]:
        count = count + level(game_level, game)   #recursive call when the call itself the change the start 
    return count
print(level(game_level,"level 1" ))