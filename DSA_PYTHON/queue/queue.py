class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self,n):
        self.queue.append(n)
        print(f" your are {self.queue}")
        
    def dequeue(self):
        if self.is_empty():
            print(f"Element is not variable in queue:{self.queue}")
        else:
            print(f"deleted element:{self.queue.pop(0)}")
            print(f" your list is :{self.queue}")
        
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f" Front:{self.queue[0]}")
            
            
    
    def is_empty(self):
        return len(self.queue) == 0
    
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f"Queue element:{self.queue}")


q = Queue()
q.enqueue(142)
q.enqueue(36)
q.enqueue(35)
q.enqueue(34)
q.enqueue(4)
q.dequeue()



        
        
# in an office mulltiple user friend requiest in single printer a printet processer they are 