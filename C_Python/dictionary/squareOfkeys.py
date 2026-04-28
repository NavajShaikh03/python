# 3. WAP to generate and print a dictionary that contains a number (between 1 and n) in the 
# form {1:1 ,…..n}.i.e {1:1,2:4,3:9,…..}
n = int(input("Enter the number which square upto n number:"))
square_no= {}
for i in range(1,n+1):
    square_no.setdefault(i,i**2)   # add each keys and its square
print(square_no)