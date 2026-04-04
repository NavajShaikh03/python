# Python docstring are the string literals that appear right after the 
# definition of a function , method ,class , of module

def square(n):
    '''Takes in a number n, return the square of n'''    # this is not a string it is a docstring write the below of function 
    print(n**2)
square(5)
print(square.__doc__)