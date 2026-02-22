# top = []

# def push():
#     if len(top) == 0:
#         top.append(776)
#         top.append('t')
#         top.append(776)
#         top.append('t')
#         pass
#     else:
#         print("Stack is not empty")
# push()
# print(top)

# def pop():
#     if len(top) == 0:
#         print("stack is empty")
#     else:
#         top.pop()
#     print(f"Element is deleted:{top}")
# print(pop())


# def peek():
#     if len(top) == 0:
#         return "Stack is empty"
#     return top[-1]
# print(peek())


while(True):
    stack =[]
    user_input = input("Enter the element:")
    print("For inserting Element tap 1:")
    print("For deleting Element tap 2:")
    print("For check status of Element tap 3:")
    print("For exiting tap 4:")

    choice = int(input("Enter you choice:"))

    if choice == 1:
        def push():
            stack.append(user_input)
        push()
        print(f"your list is {stack}")
        
    elif choice == 2:
        def pop():
            if len(stack) == 0:
                print("stack is empty")
            else:
                stack.pop()
                print(f"Element is deleted:{stack}")
        pop()
        
    elif choice == 3:
        def peek():
            if len(stack) == -1:
                return "Stack is empty"
            return stack[-1]
        print(peek())

    elif choice == 4:
        break
    
        


    