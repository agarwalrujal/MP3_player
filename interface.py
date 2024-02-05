from tkinter import *
import tkinter as tk
import pygame
from PIL import ImageTk,Image
pygame.init()
pygame.mixer.init()
m=tk.Tk(screenName='MP3 PLAYER',  baseName=None,  className='MP3 PLAYER',  useTk=1)
m.geometry("500x500")

song_list= ["Lauv - I Like Me Better (Lyrics).mp3","Andy Grammer - Back Home Lyrics.mp3","Alec Benjamin - Let Me Down Slowly (Lyrics).mp3",
"Alan Walker, Sabrina Carpenter & Farruko- On My Way.mp3","Aastha Gill - Buzz feat Badshah Priyank Sharma Official Music Video.mp3"]
T = Text(m,  height=2, width=30)
i=0

def load_play():
    global i
    pygame.mixer.music.load(song_list[i])
    pygame.mixer.music.play()
    T.delete("1.0", "end") 
    T.pack() 
    T.insert(END, song_list[i])
    
def load_nextplay():
    global i
    i=i+1
    pygame.mixer.music.load(song_list[i])
    pygame.mixer.music.play() 
    T.delete("1.0", "end") 
    T.pack() 
    T.insert(END, song_list[i])



def load_previous():
    global i
    i = i-1
    pygame.mixer.music.load(song_list[i])
    pygame.mixer.music.play() 
    T.delete("1.0", "end")  
    T.pack() 
    T.insert(END, song_list[i])
def pause():
    pygame.mixer.music.pause()

    

  
play = tk.Button(m, text='play',height=1, width=5, command=load_play)
play.place(x=250,y=400)

next_song = tk.Button(m, text='next',height=1, width=5, command=load_nextplay)
next_song.place(x=400,y=400)

before_song = tk.Button(m, text='before',height=1, width=5, command=load_previous)
before_song.place(x=100,y=400)


pause = tk.Button(m, text='pause',height=1, width=5, command=pause)
pause.place(x=250,y=300)


# Create a photoimage object of the image in the path
# image1 = Image.open("bird.png")

# test = ImageTk.PhotoImage(image1)

# label1 = tk.Label(image=test)
# label1.image = test

# # Position image
# label1.place(x=250, y=50)

# T = Text(m, height=2, width=30) 
# T.pack() 
# T.insert(END, f'{song_name}') 

m.mainloop()