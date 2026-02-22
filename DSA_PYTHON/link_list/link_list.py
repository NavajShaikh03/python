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
                   
        
            
            



# a train has coches to connect to the 
# you have list student role no. store in link list you task search give no. are found or not
# you are given link list your task is find the middle element of link list search for given 

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class linked_list:
#     def __init__(self):
#         self.head = None        
        
        
#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head= new_node
#             return
#         last = self.head
#         while last.next:
#             last=last.next
#         last.next=new_node    
        
        
#     def display(self):
#         current=self.head
#         while current:
#             print("|",current.data,end=" | ->  ")
#             current = current.next 
#         print("None")
        
        
# ll=linked_list()
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.display()


# concept of insert and deleting

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class linked_list:
#     def __init__(self):
#         self.head = None    
    
#     def insert_at_beginning(self,data):
#         new_node=Node(data)          # creat new node with head
#         new_node.next = new_node     # connectting to the exxisting head of linkList
#         self.head = new_node         #shifting head position t0 the new node
      
#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head= new_node
#             return
#         last = self.head
#         while last.next:
#             last=last.next
#         last.next=new_node    
        
#     def specific_position(self,data,position):
#         new_node = Node(data)
        
#         if position == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
        
#         temp = self.head 
        
#         for _ in range(position-1):
#             if temp is None :
#                 return
#             temp = temp.next
            
#         new_node.next = temp.next
#         temp.next = new_node
        
        
#     def display(self):
#         current=self.head
#         while current:
#             print("|",current.data,end=" | ->  ")
#             current = current.next 
#         print("None")
        
#     def delete_from_beginning(self):
#         if self.head:
#             self.head = self.head.next
            
#     def delete_from_end(self):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             return
        
#         temp = self.head
#         while temp.next.next:
#             temp = temp.next
#         temp.next =  None
        
#         def delete_by_value(self,key):
#             temp = self.head
            
#             if temp and temp.data == key:
#                 self.head = temp.next
            
#             prev = None
#             while temp and temp.data != key:
#                 prev = temp
#                 temp = temp.next
#             if temp:
#                 prev.next = temp.next
            
#         def reverse(self):
#             prev = None
#             current =self.head
            
#             while current:
#                 next_node = current.next
#                 current.next = prev
#                 prev = current
#                 current = next_node
#             self.head = prev
        
# ll=linked_list()
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.insert_at_beginning(45)
# ll.display()


# using map maintainnig linkList each node store song id you have to perform following operation
# add and start add song at end , delete song by position , search song by id and display playlist

# class Node:
#     def __init__(self,song_id):
#         self.data=song_id
#         self.next=None
# class song_list:
#     def __init__(self):
#         self.head = None    
    
#     def add_at_beginning(self,song_id):
#         new_song = Node(song_id)          # creat new node with head
#         new_song.next = new_song     # connectting to the exxisting head of linkList
#         self.head = new_song         #shifting head position t0 the new node
      
#     def append(self,song_id):
#         new_song = Node(song_id)
#         if self.head is None:
#             self.head= new_song
#             return
#         last = self.head
#         while last.next:
#             last=last.next
#         last.next=new_song    
        
#     def specific_position(self,song_id,position):
#         new_song = Node(song_id)
        
#         if position == 0:
#             new_song.next = self.head
#             self.head = new_song
#             return
        
#         temp_song = self.head 
        
#         for _ in range(position-1):
#             if temp_song is None :
#                 return
#             temp_song = temp_song.next
            
#         new_song.next = temp_song.next
#         temp_song.next = new_song
        
        
#     def display(self):
#         current=self.head
#         while current:
#             print("|",current.song_id,end=" | ->  ")
#             current = current.next 
#         print("None")
        
#     def delete_from_beginning(self):
#         if self.head:
#             self.head = self.head.next
            
#     def delete_from_end(self):
#         if self.head is None:
#             return 
#         if self.head.next is None:
#             return
        
#         temp_song = self.head
#         while temp_song.next.next:
#             temp_song = temp_song.next
#         temp_song.next =  None
        
#         def delete_by_id(self,key):
#             temp_song = self.head
            
#             if temp_song and temp_song.song_id == key:
#                 self.head = temp_song.next
            
#             prev = None
#             while temp_song and temp_song.song_id != key:
#                 prev = temp_song
#                 temp_song = temp_song.next
#             if temp_song:
#                 prev.next = temp_song.next
        
# ll=song_list()
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.append(10)    
# ll.insert_at_beginning(45)
# ll.display()






# Node for Linked List
# class Node:
#     def __init__(self, song_id):
#         self.song_id = song_id
#         self.next = None


# class Playlist:
#     def __init__(self):
#         self.head = None
#         self.song_map = {}   # map: song_id -> node

#     def add_at_start(self, song_id):
#         if song_id in self.song_map:
#             print("Song ID already exists")
#             return

#         new_node = Node(song_id)
#         new_node.next = self.head
#         self.head = new_node
#         self.song_map[song_id] = new_node
#         print("Song added at start")

#     def add_at_end(self, song_id):
#         if song_id in self.song_map:
#             print("Song ID already exists")
#             return

#         new_node = Node(song_id)

#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node

#         self.song_map[song_id] = new_node
#         print("Song added at end")

#     def delete_by_position(self, position):
#         if self.head is None:
#             print("Playlist is empty")
#             return

#         if position == 1:
#             removed = self.head
#             self.head = self.head.next
#             del self.song_map[removed.song_id]
#             print("Song deleted")
#             return

#         temp = self.head
#         prev = None
#         count = 1

#         while temp and count < position:
#             prev = temp
#             temp = temp.next
#             count += 1

#         if temp is None:
#             print("Invalid position")
#             return

#         prev.next = temp.next
#         del self.song_map[temp.song_id]
#         print("Song deleted")

#     def search_by_id(self, song_id):
#         if song_id in self.song_map:
#             print("Song found:", song_id)
#         else:
#             print("Song not found")

#     def display_playlist(self):
#         if self.head is None:
#             print("Playlist is empty")
#             return

#         temp = self.head
#         print("Playlist:")
#         while temp:
#             print(temp.song_id, end=" -> ")
#             temp = temp.next
#         print("NULL")



# playlist = Playlist()

# playlist.add_at_start(101)
# playlist.add_at_end(102)
# playlist.add_at_end(103)
# playlist.display_playlist()
# playlist.search_by_id(102)
# playlist.delete_by_position(2)
# playlist.display_playlist()




# hospital emergency ward  manages patients using link list each patients is register in the order they arrived but critical patients can be moved in the q each patients contain patients_id , and save Id  
# implement a linkedList with following operation:
# 1. register patient
# 2. Insert patients in such a way that :
#     patients with higher severity is comes before lower severity
#     order among  same severity is preserved
# 3.Discharge first patient 
# 4.Discharged patient by id
# 5.search patient 
# 6.Display patients queue
# 7.Count total patients


