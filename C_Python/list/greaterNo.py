number_of_list = [1,2,3,4,5,6,7,8,9,10,0,56,7,3,67,34,98,92,45,23]
small_number = int(input("Enter the number which to find the greater values no.:"))
print("\n")

total_greater_no = 0    # total count the greater number 
for number in number_of_list:
    if small_number < number:
        print(f"greater number then {small_number} from list is :",number)
        total_greater_no+=1
print(f"\nTotal grater number then {small_number} is :",total_greater_no)