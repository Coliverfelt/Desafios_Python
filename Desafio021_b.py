# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Independente do uso de funcionalidades que são dependentes de sistema operacional.
# Para este código é necessário copiar o arquivo antes e colar na pasta do projeto dentro da IDE (no meu caso PyCharm)
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('Kalimba.mp3')
pygame.mixer.music.play()
pygame.event.wait()
