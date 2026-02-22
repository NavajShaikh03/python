# dsing broser histroy steyem using doubly link list that suppose visiting to new page moving backword monving to forwered

class Node:
    def __init__(self,page):
        self.page = page
        self.prev = None
        self.next = None

class History:
    def __init__(self):
        self.head = None
    
    def append(self,page):
        new_page = Node(page)
        
        if self.head is None:
            self.head = new_page
            return
        
        last = self.head
        
        while last.next:
            last = last.next
        last.next = new_page
        new_page.prev = last
        
        def display(self):
            current = self.head 
            while current:
                print(f"{current.page}",end="->")
                current =current.next
            print("None")
            
        def reverse(self):
            current = self.head
            if not current:
                return
            
            while current:
                print(f"{current.page}",end ="->")
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
            self.head
            
            
            
            
            #
            while current :
                if current.page == key:
                    current.prev.next = current.next
                    
                    if current.next:
                        current.next.prev = current.prev
                    print(f"{key} is deleted")
                    return
                current = current.next
            print(f"{key} is not found")
            
d = History()
d.append(13)
d.append(43)
d.append(23)
d.search(13)
        