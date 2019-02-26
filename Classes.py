#!/usr/bin/python3
#format:utf-8

import pygame

class Joueur:
    """définit les joueurs"""

    def __init__ (self, couleur, points, vie, current_bonuses):
        self.current_bonuses = current_bonuses
        self.couleur = couleur
        self.points = points
        self.vie = vie
        

class Brique:
    """défintition d'une brique"""
    bonus = [barre_rapide, balle_rapide, plusieurs_balles, balle_plus_rapide_cmp_adv]
    malus = [barre_lente, indicateur_inv, commandes_inverse, ecran_sombre_adv, barre_bonus, balle_plus_lente]
    def __init__ (self, statut, bonus, malus):
    
