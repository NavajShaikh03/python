class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class Circular:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        current= self.head     # pointer chi value pointer madhe current
        while current != self.head:      
            current = current.next
            
        new_node.next = self.head    # connect first node
        current.next = new_node
        self.head = new_node
        
        
    def insert_at_end(self,data):
        new_node = Node(data)
            
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
            
        temp = self.head
        while temp.next != self.head:
            temp = temp.next  
                
        temp.next = new_node
        new_node.next = self.head
                
    def search(self,key):
        if self.head is None:
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp=temp.next
            if temp == self.head:
                break
        return False
            
    def insert_after(self,key,data):
        if self.head is None:
            return
        temp = self.head
        while True:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
            
    def delete_by_value(self,key):
        if self.head == None:
            print("list is empty")
            return
        current = self.head
        if current.data ==key:
            if current.next == self.head:
                self.head = None
                return
            
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = current.next
            last.next = self.head
            return
        
        prev= current
        current = current.next
        while current != self.head:  # ha part 
            if current.data == key:
                prev.next=current.next 
                return
            prev =current
            current = current.next 
        print("Value are not found")      
        
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        
        temp = self.head     # start from here
        while True:
            print(temp.data, end = "->")
            temp=temp.next
            if temp == self.head:
                break
        print("back to head")
        
cl = Circular()
cl.insert_at_beginning(10)
cl.insert_at_beginning(20)
cl.insert_at_beginning(30)
cl.insert_at_beginning(40)
cl.display()
print("--------After adding at end---------")
cl.insert_at_end(10)
cl.insert_at_end(20)
cl.display()
print("----searching----")
print(cl.search(10))
print(cl.search(100))
print("----insert after----")   
cl.insert_after(20,25)
cl.display()
cl.delete_by_value(40)
cl.delete_by_value(25)

cl.display()



# Q.7 : A Music app plays music in loop meaning after the last song it starts from first. Implement it using circular linked list. Add Songs and Add a function like You have 5 songs and Select Play is shows Playing Song A then Select next it shows Playing Song B and so on. After Last Song it should play First Song