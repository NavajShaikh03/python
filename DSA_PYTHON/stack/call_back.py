#Q. in a customer center when support agent handle calls
# 1.if a new urgent call comes it should be handled
#2. most recent call is completed first
#creare a program , call handling system using stack
# should allow first reciev the call end the current call (pop top caller id from stack), display which call has ended if there are no call display message 
#display caller id currently handle
# check the pending call waiting in the stack

top = []

def push():
    if len(top) == 0:
        top.append(776)
        top.append('t')
        top.append(776)
        top.append('t')
        pass
    else:
        print("Stack is not empty")
push()
print(top)

def pop():
    if len(top) == 0:
        print("stack is empty")
    else:
        top.pop()
    print(f"Element is deleted:{top}")
print(pop())


def peek():
    if len(top) == 0:
        return "Stack is empty"
    return top[-1]
print(peek())