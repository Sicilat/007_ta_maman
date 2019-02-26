#!/usr/bin/python3
#format:utf-8

from pygame import

class Joueur:
    """définit les joueurs"""

    def __init__ (self, couleur, points, vie, current_bonuses):
        self.current_bonuses = current_bonuses
        self.couleur = couleur
        self.points = points
        self.vie = vie

class Brique:
    """défintition d'une brique"""
    def __init__ (self, statut):
        self.statut = statut
