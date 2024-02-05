song_list= ["[LYRICS] Seven Lions, SLANDER & Dabin - First Time (feat. Dylan Matthew)",
"All The World (I Tell Myself)"]
import tkinter
from pygame import *
pygame.init()
pygame.mixer.init()
def next_pressed():
    for i in range(len(song_list)):
        print(i)
        song_name=f"{song_list[i+1]}.mp3"
        print(song_name)
        # playsound(song_name)
        break
def play():
    pygame.mixer.music.load(next_pressed())
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()



