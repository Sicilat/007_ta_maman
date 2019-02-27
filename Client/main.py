#!/usr/bin/python

import os, sys
import pygame
from pygame.locals import *
from Classes import *

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
    print(fullname)
    image = pygame.image.load(fullname).convert()
    return image, image.get_rect()

def Padmove(key, pad):
    if key[K_RIGHT]:
        Pad.sprite(pad, "right")
    if key[K_LEFT]:
        Pad.sprite(pad, "left")   

pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('V-Bricks')

background, backgroundrect = load_image('background.png')

display_window = 1

pad = Pad()

while display_window:
    for event in pygame.event.get():
        if event.type == QUIT:
            display_window = 0
        key = pygame.key.get_pressed()
        Padmove(key, pad)
        screen.blit(background, (0, 0))
        screen.blit(pad.direction, (pad.x , pad.y))
        pygame.display.flip()
        