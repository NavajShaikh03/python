string = ["hello","world" , "python", "programming"]
print(string)
search_string = input("Enter the string to search:")
if search_string in string:
    print(f"{search_string} is found in the list.")
else:
    print("your string is wrong and Enter the string in present in the list: ")