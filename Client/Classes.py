#!/usr/bin/python3
#format:utf-8

import pygame
from pygame.locals import *
from utils import *

class Joueur:
    """définit les joueurs"""

    def __init__ (self, couleur, points, vie, current_bonuses, max_X, min_X):
        self.current_bonuses = current_bonuses
        self.couleur = couleur
        self.points = points
        self.vie = vie
        self.max_X = max_X
        self.min_X = min_X
        

class Brique:
    """défintition d'une brique"""
    

PAD_SPRITE_WIDTH = 485
PAD_SPRITE_HEIGHT = 128

class Pad:
        def __init__(self):
                self.move = []

                sprite_sheet = SpriteSheet("data/sprite_pad.png")

                image = pygame.transform.scale(sprite_sheet.get_image(0, 0, PAD_SPRITE_WIDTH, PAD_SPRITE_HEIGHT).convert_alpha(), (242, 64))
       	        self.move.append(image)
       	        image = pygame.transform.scale(sprite_sheet.get_image(0, 128, PAD_SPRITE_WIDTH, PAD_SPRITE_HEIGHT).convert_alpha(), (242, 64))
                self.move.append(image)
    
                self.case_x = 0
                self.direction = self.move[0]
                self.frame = 0
                self.x = 0
                self.y = 0
    
        def sprite(self, direction):            
                if direction == 'right':
                    if self.case_x < (1080 - 30):
                        self.case_x += 1.5
                        self.x = self.case_x
                    self.direction = self.move[self.frame]
                    self.frame += 1
                    if self.frame > 1:
                        self.frame = 0
                        
                if direction == 'left':
                    if self.case_x > 0:
                        self.case_x -= 1.5
                        self.x = self.case_x
                    self.direction = self.move[self.frame]
                    self.frame += 1
                    if self.frame > 1:
                        self.frame = 0

class SpriteSheet(object):

		sprite_sheet = None

		def __init__(self, file_name):
 
				self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
		def get_image(self, x, y, width, height):

				image = pygame.Surface([width, height]).convert()
 
				image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

				for i in range(0, 256):
						image.set_colorkey((i, i, i))

				return image
