#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:02:18 2022

@author: raphael.bouvet@Digital-Grenoble.local
"""

from board import Board

class Partie:
    def __init__(self):
        self.board=Board()
        position_debut=[[(3,3),"Blanc"],[(4,4),"Blanc"],[(3,4),"Noir"],[(4,3),"Noir"]]
        for pion in position_debut:
            self.board.placePion(pion[0], pion[1],True)
        self.findepartie=False
        
    def menu(self):
        print("========== Othello version 1 ========")
        print("Actuellement seulement la version deux joueur est disponible")
        print("Appuyer sur Entrée pour continuer et n'importe quelle touche pour quitter")
        choix=input()
        if choix =='':
            self.partie()
        else:
            exit()
        
        
    def partie(self):
        tour=0
        self.board.printBoard()
        while not self.findepartie:
            couleur_joueur=self.detJoueur(tour)
            tour_valide=False
            while not tour_valide:
                self.board.printBoard()
                print(f"Joueur {couleur_joueur}: A toi de jouer")
                print("Ligne :")
                row=int(input())
                print("Colonne :")
                col=int(input())
                tour_valide = self.board.placePion((row-1,col-1), couleur_joueur)
            tour += 1
            
    def detJoueur(self,tour):
        if tour%2==0:
            return 'Noir'
        else:
            return 'Blanc'
        
    def checkFinDePartie(self):
        
        self.findepartie==True
        
partie=Partie()
partie.menu()