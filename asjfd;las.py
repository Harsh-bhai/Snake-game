import pygame
import time
pygame.mixer.init()

def playsongwav(song):
    pygame.mixer.music.load(f"./{song}.wav")
    while True:
        pygame.mixer.music.play(1)
        return True
def playsongwavStop():
    pygame.mixer.music.stop()


playsongwav("opening_song")
time.sleep(3)
playsongwavStop()
