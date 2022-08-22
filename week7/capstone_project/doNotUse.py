# Add songs to a playlist
# Remove songs from a playlist
# Play the current selected song, default is the first song on the playlist
# Skip to the next song on the playlist. If at end of list, restart from the beginning
# Go back to the previous song on the playlist.  If at the start, go back to the end of the list.
# Randomly shuffle the song list
# Show Currently Playing Song
# Show Current Playlist Order
from random import randint
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def setTitle(self):
        self.title = title

    def getArtist(self):
        return self.artist

    def setArtist(self):
        self.artist = artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))



class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self):
        return self.count

    def first(self):
        return self.head
    
    def last(self):
        return self.tail


    def addFirst(self, data):
        # Add a node at the front of the list
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.count += 1
       

    def addLast(self, data):
        # Add a node at the end of the list
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            node.prev = temp
        self.count += 1


    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        temp = self.head
        found = 0
        index = -1
        if temp != None:
            while temp != None:
                index +=1 
                if temp.data == data:
                    found += 1 
                    break
                temp = temp.next
            if found == 1:
                print(index)
            else:
                print("Item not found")
        else:
            print("The list is currenly empty")
            


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return 
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def shuffle(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next != None:
                index= current.next
                while index != None:
                    if (randint(0,1) == 1):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

   
      
class Playlist:
    def __init__(self):
        self.s_list = []
        self.count = 0 

    def addMusic(self,title, artist):
        newSong = Song(title,artist)
        self.s_list.append(newSong)
        self.count += 1

    def removeMusic(self):  #2
        self.s_list.deleteAtIndex()

    # def playMusic(self): 
    # def skipMusic(self):
    # def goBack(self):
    # def shuffleMusic(self):
    # def whatsPlaying(self):

    def getAll(self):
        results = []
        for song in self.s_list:
            results.append(song)
            print(song)
        return results

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


mySongs = DoublyLinkedList()

myPlayList = Playlist()
myPlayList.addMusic("Raging on a Sunday", "Bohnes")
myPlayList.addMusic("Queen of Broken Hearts", "Blackbare")
myPlayList.addMusic("King of the Clouds", "Panic! at the Disco")
myPlayList.addMusic("Holy", "King Princess")
myPlayList.addMusic("Cancer", "Twenty One Pilots")
myPlayList.addMusic("Playinwitme", "Kyle,Kehlani")

while True:
    menu()
    choice = int(input())

    if choice == 1:
        title = input("Please inter the sonf title: ")
        artist = input("Please enter the song artist: ")
        myPlayList.addMusic(title,artist)
        
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title
        title = input("Please enter the song title you would like to remove: ")
         # remove song from playlist
        here = mySongs.indexOf(f"{title}") #2
        while True:
            mySongs.deleteAtIndex(here)
            
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")
        print()        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        myPlayList.getAll()
    elif choice == 0:
        print("Goodbye.")
        break

            
