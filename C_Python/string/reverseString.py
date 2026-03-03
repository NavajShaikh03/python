# 20. Write a Python function to reverse a string if its length is a multiple of 4.

def reverse_string(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return print("The length of the string is not a multiple of 4 :your string is",string)

input_string = input("Enter a string:")
result = reverse_string(input_string)
print("Reversed String:",result)


# other way


def r_string(text):
    
    if len(text) % 4 == 0:
        reversed =





text = input("Enter  string:")

    
