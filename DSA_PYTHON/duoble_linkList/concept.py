class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly:
    def __init__(self,):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        
        def display(self):
            current = self.head 
            while current:
                print(f"{current.data}",end="->")
                current =current.next
            print("None")
            
        def reverse(self):
            current = self.head
            if not current:
                return
            
            while current:
                print(f"{current.data}",end ="->")
                current = current.prev
            print("None")
            
        def search(self,key):
            current = self.head
            position = 0
            while current:
                if current.data == key:
                    print(f"{key} found at {position}")
                    return
                current = current.next
                position +=1
            print(f"{key} not found")
            
        def delete(self,key):
            current = self.head

            if current.data ==key:
                self.head = current.next
                
                if self.head:
                    self.head.prev = None
                print(f"{key} is deleted")
                return
        
            #  if data at middle  or at end
            while current :
                if current.data == key:
                    current.prev.next = current.next
                    
                    if current.next:
                        current.next.prev = current.prev
                    print(f"{key} is deleted")
                    return
                current = current.next
            print(f"{key} is not found")
            
d = Doubly()
d.append(13)
d.append(43)
d.append(23)
d.search(13)
        