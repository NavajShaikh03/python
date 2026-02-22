# Q.7 : A Music app plays music in loop meaning after the last song it starts from first. Implement it using circular linked list. Add Songs and Add a function like You have 5 songs and Select Play is shows Playing Song A then Select next it shows Playing Song B and so on. After Last Song it should play First Song

class Song:
    def __init__(self,song_name):
        self.song_name = song_name
        self.next = None
        
class SongPlay:
    def __init__(self):
        self.head = None
    
    def add_song(self,song_name):
        new_song = Song(song_name)
        if self.head is None:
            self.head = new_song
            new_song.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        
        last.next=new_song
        new_song.next = self.head
                
    def play_next(self):
        # print(f"playing {self.current.name}")
        # self.current = self.current.next
        if self.head is None:
            print("No songs available to play.")
            return
        print("Playing songs in loop:")
        current = self.head
        while True:
            print(f"Playing: {current.song_name}")
            current = current.next
            if current == self.head:
                break
        
s = SongPlay()
s.add_song("Song A")
s.add_song("Song B")
s.add_song("Song C")
s.add_song("Song d")

s.play_next()
s.play_next()