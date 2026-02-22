# it is complete binary tree tree and there are two types main heap tree and max heap tree
# formula is calculate the last node is D=(l/2)-1 
# l = 2 * D + 1
# r =2 * D + 1


class HeapTree:
    def __init__(self):
        self.heap = []
    def heapify(self,n,p):
        l=2*p+1
        r=2*p+2
        smallest =p
        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != p:
            self.heap[smallest],self.heap[p] = self.heap[p],
            self.heapify(n,smallest)
    def insert(self,v):
        if len(self.heap)==0:
            self.heap.append(v)
        else:
            self.heap.append(v)
            for i in range((self.heap) // 2-1,-1,-1):
                self.heapify(len(self.heap),i)
h = HeapTree()
h.insert(20)
h.insert(34)
h.insert(25)
h.insert(24)
h.insert(22)
h.insert(87)
h.insert(23)
h.insert(21)
print(h.heap)
