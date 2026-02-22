class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head = None        
        
        
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head= new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next=new_node    
        
        
    def display(self):
        current=self.head
        while current:
            print("|",current.data,end=" | ->  ")
            current = current.next 
        print("None")
        
        
ll=linked_list()
ll.append(10)    
ll.append(10)    
ll.append(10)    
ll.append(10)    
ll.append(10)    
ll.append(10)    
ll.append(10)    
ll.append(10)    
ll.display()