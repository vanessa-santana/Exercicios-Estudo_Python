#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#salvar o arquivo mp3 na mesma pasta

import pygame

pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()