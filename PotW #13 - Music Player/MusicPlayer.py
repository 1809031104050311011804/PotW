#The bulk of this code is sourced from:
#https://dev.to/kalebu/make-your-own-python-music-player-44n


from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
import random


class music_player:
    def __init__(self, window):
        global label_song_name_exists, song_status, label_song_status
        
        window.geometry("400x140")
        window.title("MUSIC PLAYER")
        window.resizable(0, 0)

        button_load = Button(window, text='LOAD', width=10, font=("Times",10), command=self.load)
        button_play = Button(window, text="PLAY", width=10, font=("Times",10), command=self.play)
        button_pause = Button(window, text="PAUSE", width=10, font=("Times",10), command=self.pause)
        button_stop = Button(window, text="STOP", width=10, font=("Times",10), command=self.stop)

        button_load.place(x=5, y=5)
        button_play.place(x=5, y=40)
        button_pause.place(x=5, y=75)
        button_stop.place(x=5, y=110)

        self.music_file = False
        self.playing_state = False

        label_song_name_exists = False
        
        song_status = "NO SONG LOADED"
        label_song_status = Label(font=("Times",10))
        label_song_status.place(relx=0.6, rely=0.125, anchor=CENTER)
        label_song_status.config(text=song_status, bg="black", fg="white")


    def load(self):
        global label_song_name_exists, label_song_name, color
        
        mixer.init()
        mixer.music.stop()

        self.music_file = filedialog.askopenfilename()

        if label_song_name_exists == True:
            label_song_name.destroy()
            label_song_name_exists = False

        music_file_path = self.music_file
        music_file_name = os.path.basename(music_file_path).split(".")[0]

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        color = "#{:02x}{:02x}{:02x}".format(r, g, b)

        root.config(bg=color)

        label_song_name = Label(text=music_file_name , font=("Times",10))
        label_song_name.place(relx=0.6, rely=0.5, anchor=CENTER)
        label_song_name_exists = True
        song_status = "SONG LOADED"
        label_song_status.config(text=song_status, bg=color, fg="white")
        

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

            song_status = "PLAYING"
            label_song_status.config(text=song_status, bg=color, fg="white")


    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self_playing_state = True

            song_status = "PAUSED"
            label_song_status.config(text=song_status, bg=color, fg="white")

        else:
            mixer.music.unpause()
            self.playing_state = False

            song_status = "PLAYING"
            label_song_status.config(text=song_status, bg=color, fg="white")


    def stop(self):
        mixer.music.stop()

        label_song_name.destroy()
        label_song_name_exists = False

        song_status = "NO SONG LOADED"
        label_song_status.config(text=song_status, bg="black", fg="white")

        root.config(bg="black")


root = Tk()
root.config(bg="black")
MusicPlayer = music_player(root)
root.mainloop()