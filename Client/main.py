#!/usr/bin/python3

import os, sys
import pygame
from pygame.locals import *

message = "error 404"

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    sound = pygame.mixer.Sound(fullname)
    return sound

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    return image, image.get_rect()

pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('V-Bricks')

display_window = 1

while display_window:
    for event in pygame.event.get():
        if event.type == QUIT:
            display_window = 0