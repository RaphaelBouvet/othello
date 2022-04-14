#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:02:18 2022

@author: raphael.bouvet@Digital-Grenoble.local
"""

from board import Board
from joueur import Joueur

class Partie:
    def __init__(self):
        self.board=Board()
        position_debut=[[(3,3),"Blanc"],[(4,4),"Blanc"],[(3,4),"Noir"],[(4,3),"Noir"]]
        for pion in position_debut:
            self.board.placePion(pion[0], pion[1],True)
        self.findepartie=False
        self.listeJoueurs=['','']
    
    def initJoueurs(self,choix):
        listecouleur=['Blanc','Noir']
        print("Rentrer le nom du premier joueur")
        nom=input()
        print("Choix de la couleur : Noir, Blanc")
        couleur=input()
        new_joueur=Joueur(nom,couleur)
        listecouleur.remove(couleur)
        if choix=='a':
            print("Rentrer le nom du deuxième joueur")
            nom=input()
            joueur_restant=Joueur(nom,listecouleur[0])
        else:
            joueur_restant=Joueur('AI',listecouleur[0],True)
        self.addJoueur(new_joueur)
        self.addJoueur(joueur_restant)
    
    def initAuto(self):
        new_joueur=Joueur('AI_1','Noir',True)
        joueur_restant=Joueur('AI_2','Blanc',True)
        self.addJoueur(new_joueur)
        self.addJoueur(joueur_restant)

        
    def addJoueur(self,joueur):
        if joueur.couleur=='Noir':
            self.listeJoueurs[0]=joueur
        else:
            self.listeJoueurs[1]=joueur
        
    def menu(self):
        print("========== Othello version 2 ========")
        print("a) mode JvsJ")
        print("b) vs AI")
        print("c) mode auto AI vs AI")
        choix=input('Choix : ')
        if choix =='a' or choix=='b':
            self.initJoueurs(choix)
            self.partie()
        elif choix =='c':
            self.initAuto()
            self.partie(True)
        else:
            exit()
            
    def partie(self,mode_auto=False):
        tour=0
        self.board.printBoard()
        while not self.findepartie:
            joueur_actuel=self.detJoueur(tour)
            self.checkFinDePartie
            tour_valide=False
            while not tour_valide:
                self.board.printBoard()
                print(f"Joueur {joueur_actuel.nom} {joueur_actuel.couleur}: A toi de jouer")
                if not joueur_actuel.AI:
                    print("Ligne :")
                    row=int(input())
                    print("Colonne :")
                    col=int(input())
                    tour_valide = self.board.placePion((row-1,col-1), joueur_actuel.couleur)
                else:
                    row,col=joueur_actuel.randomChoice(self.board)
                    print(f" position testée {row} {col}")
                    tour_valide = self.board.placePion((row,col), joueur_actuel.couleur)
            tour += 1
            self.checkFinDePartie(self.detJoueur(tour))
            # if mode_auto:
            #     wait=input()
        self.finPartie()
            
    def detJoueur(self,tour):
        if tour%2==0:
            return self.listeJoueurs[0]
        else:
            return self.listeJoueurs[1]
        
    def checkFinDePartie(self,joueur):
        self.findepartie=self.board.checkBoardsolved(joueur.couleur)
        
    def finPartie(self):
        self.board.printBoard()
        self.board.score()
        print("Fin de la Partie")
        print(f"Score Noir : {self.board.score_black}")
        print(f"Score Blanc : {self.board.score_white}")
        
partie=Partie()
partie.menu()