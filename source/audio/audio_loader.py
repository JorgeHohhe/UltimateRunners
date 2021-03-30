import pygame
import tkinter as tkr

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)


def play_music_map(level):
    if level == 1:
        pygame.mixer.music.load("source/audio/sounds/Noisestorm - Barracuda.mp3")
        pygame.mixer.music.play()
    elif level == 2:
        pygame.mixer.music.load("source/audio/sounds/Nitro Fun - New Game.mp3")
        pygame.mixer.music.play()
    elif level == 3:
        pygame.mixer.music.load("source/audio/sounds/Urbanstep - Icebreaker.mp3")
        pygame.mixer.music.play()
    elif level == 4:
        pygame.mixer.music.load("source/audio/sounds/Virtual Riot - Idols.mp3")
        pygame.mixer.music.play()
    elif level == 5:
        pygame.mixer.music.load("source/audio/sounds/Danimal Cannon - Long Live The New Fresh.mp3")
        pygame.mixer.music.play()


def death_sound():
    pygame.mixer.music.load("source/audio/sounds/DeathSoundEffect.mp3")
    pygame.mixer.music.play()


def set_volume(val):
    volume = int(val)/100
    pygame.mixer.music.set_volume(volume)


def pause_menu():
    pygame.mixer.music.pause()
    setter = tkr.Tk()
    setter.title("Audio Player")
    # setter.geometry("205x400")
    VolumeLevelImg = tkr.PhotoImage(file='source/graphics/images/cube.png')
    VolumeLevel = tkr.Scale(setter, label='Volume', activebackground='blue', from_=0, to=100, orient=tkr.HORIZONTAL, resolution=1, command=set_volume)
    quitter = tkr.Button(setter, image=VolumeLevelImg, text="Quit", command=setter.destroy)
    VolumeLevel.pack()
    quitter.pack()
    setter.mainloop()
    pygame.mixer.music.unpause()
