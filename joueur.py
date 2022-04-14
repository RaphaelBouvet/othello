#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:51:20 2022

@author: raphael.bouvet@Digital-Grenoble.local
"""
import random

class Joueur:
    def __init__(self,nom,couleur,AI=False):
        self.couleur=couleur
        self.nom=nom
        self.AI=AI
        
    def Choice(self,board):
        return self.randomChoice(board)
    
    def randomChoice(self,board):
        self.current_board=board
        # check valid position 
        liste_pos_valide=[]
        for row in self.current_board.arr:
            for pion in row:
                pos_valide,__= self.current_board.valide_position_ai(pion.position,self.couleur)
                if pos_valide:
                    liste_pos_valide.append(pion.position)
                    print(f"position valides ? {pion.position}")
        #choose position at random
        position_choisie=random.choice(liste_pos_valide)
        return position_choisie
        