#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:51:20 2022

"""
import random
import copy
# from choiceArr import ChoiceArr

class Joueur:
    def __init__(self,nom,couleur,AI=False,AI_type='random'):
        self.couleur=couleur
        self.nom=nom
        self.AI=AI
        self.AI_type=AI_type
        
    def creationAdversaire(self):
        couleur_adverse='Noir' if self.couleur=='Blanc' else 'Blanc'
        self.adversaire=Joueur("Adversaire",couleur_adverse,AI=True,AI_type='random')
        
    def Choice(self,board):
        if self.AI_type=='random':
            return self.randomChoice(board)
        else:
            return self.best_choice(board)
    
    def randomChoice(self,board):
        current_board=board
        # check valid position 
        liste_pos_valide=[]
        for row in current_board.arr:
            for pion in row:
                pos_valide,__= current_board.valide_position_ai(pion.position,self.couleur)
                if pos_valide:
                    liste_pos_valide.append(pion.position)
        #choose position at random
        position_choisie=random.choice(liste_pos_valide)
        return position_choisie
        
    def best_choice(self,board):
        current_board=board.duplicate()
        liste_pos_valide=[]
        for row in current_board.arr:
            for pion in row:
                pos_valide,__= current_board.valide_position_ai(pion.position,self.couleur)
                if pos_valide:
                    liste_pos_valide.append(pion.position)
        simulated_board=[current_board.duplicate() for position in liste_pos_valide]
        liste_score=[]
        for new_board,pos in zip(simulated_board,liste_pos_valide):
            new_board.placePion(pos,self.couleur)
            new_board.score()
            black=new_board.score_black
            white=new_board.score_white
            liste_score.append((pos,black,white))
        for (position,black,white) in liste_score:
            score_max_couleur=0
            best_position=0
            if self.couleur=='Blanc':
                if white>=score_max_couleur:
                    score_max_couleur=white
                    best_position=position
            else:
                if black>=score_max_couleur:
                    score_max_couleur=white
                    best_position=position
        return best_position
    
    # def tree_board():

        
        

            