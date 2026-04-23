# 27. Display square of odd numbers between 1 to 20 using list comprehension


odd_square = [odd**2 for odd in range(1,21,2)]    ## this is the range of for loop use jump the after 2 steps 
print(odd_square)

# other way to solve this it 

odd_no_square = [ odd*odd  for odd in range(1,21) if odd % 2 !=0 ]
print(odd_no_square)