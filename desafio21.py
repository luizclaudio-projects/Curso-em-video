# Faça um player de mp3

import pygame

pygame.init()

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue
