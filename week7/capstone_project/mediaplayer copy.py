# Add songs to a playlist
# Remove songs from a playlist
# Play the current selected song, default is the first song on the playlist
# Skip to the next song on the playlist. If at end of list, restart from the beginning
# Go back to the previous song on the playlist.  If at the start, go back to the end of the list.
# Randomly shuffle the song list
# Show Currently Playing Song
# Show Current Playlist Order

import doubly_linked

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def __str__(self):
        return self.title + " by " + self.artist + " | "

    def __eq__(self, other):
        return ((self.title) == (other.title))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
   
      
class MediaPlayer:
    def __init__(self):
        self.playlist = doubly_linked.DoublyLinkedList()
        self.currentlyPlaying = None

    def addMusic(self,title, artist): #1
        newSong = Song(title,artist)
        self.playlist.add(newSong)
        self.playlist.count += 1

    def removeMusic(self,index):  #2
        # print(index,"index at 50")
        self.playlist.deleteAtIndex(index)


    def playMusic(self, song=None): #3
        if song:
            self.currentlyPlaying = song
        if not self.currentlyPlaying:
            self.currentlyPlaying = self.playlist.first()
        print(self.currentlyPlaying.data.getTitle())

    def skipMusic(self): #4
        self.currentlyPlaying = self.currentlyPlaying.next
        if self.currentlyPlaying == None:
            self.currentlyPlaying = self.playlist.first()
            self.playMusic(self.currentlyPlaying)

    def goBack(self): #5
        self.currentlyPlaying = self.currentlyPlaying.prev
        if self.currentlyPlaying == None:
            self.currentlyPlaying = self.playlist.last()
            self.playMusic(self.currentlyPlaying)

    def shuffleMusic(self): #6
        self.playlist.shuffle()
        print(self.playlist)

    def whatsPlaying(self): #7
        if self.currentlyPlaying:
            print(self.currentlyPlaying.data)
        else:
            print("No songs are playing")


    # def getAll(self): #8
    #     for i in self.playlist:
    #         print(i)
        

myMusic = MediaPlayer()

myMusic.addMusic("Raging on a Sunday", "Bohnes")
myMusic.addMusic("Queen of Broken Hearts", "Blackbare")
myMusic.addMusic("King of the Clouds", "Panic! at the Disco")
myMusic.addMusic("Holy", "King Princess")
myMusic.addMusic("Cancer", "Twenty One Pilots")
myMusic.addMusic("Playinwitme", "Kyle,Kehlani")


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


while True:
    menu()
    choice = int(input())

    if choice == 1:
        title = input("Please inter the sonf title: ")
        artist = input("Please enter the song artist: ")
        myMusic.addMusic(title,artist)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title
        print("\nSong list:\n")
        print(myMusic.playlist)
        removeTitle = input("Please enter the title of the song you would like to delete: ")
        remove = myMusic.playlist.indexOf(removeTitle)
        print(remove, "remove at 127")
        myMusic.removeMusic(remove)

         # remove song from playlist
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Now Playing....")        
        myMusic.playMusic()
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")  
        myMusic.skipMusic()                   
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
        myMusic.goBack()
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....") 
        myMusic.shuffleMusic() 
        # print(myMusic.playlist)  
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ") 
        myMusic.whatsPlaying()
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(myMusic.playlist)
        #myMusic.getAll()
        
        
    elif choice == 0:
        print("Goodbye.")
        break

            
