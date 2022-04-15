#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:02:18 2022

"""

from board import Board
from joueur import Joueur

class Partie:
    def __init__(self,nbjoueur,AI_type='random'):
        self.nbjoueur=nbjoueur
        self.board=Board()
        position_debut=[[(3,3),"Blanc"],[(4,4),"Blanc"],[(3,4),"Noir"],[(4,3),"Noir"]]
        for pion in position_debut:
            self.board.placePion(pion[0], pion[1],True)
        self.findepartie=False
        self.listeJoueurs=['','']
        self.AI_type=AI_type
        self.initJoueurs()
        
    def initJoueurs(self):
        listecouleur=['Blanc','Noir']
        if self.nbjoueur>0:
            print("Rentrer le nom du premier joueur")
            nom=input("Nom : ")
            print("Choix de la couleur : Noir, Blanc")
            couleur=input("Couleur :")
            new_joueur=Joueur(nom,couleur)
            listecouleur.remove(couleur)
            if self.nbjoueur==2:
                print("Rentrer le nom du deuxième joueur")
                nom=input()
                joueur_restant=Joueur(nom,listecouleur[0])
            else:
                joueur_restant=Joueur('AI',listecouleur[0],True,self.AI_type)
            self.addJoueur(new_joueur)
            self.addJoueur(joueur_restant)
        else:
            self.initAuto()
    
    def initAuto(self):
        AI_1='AI_'+ self.AI_type[0]
        AI_2='AI_'+ self.AI_type[1]
        new_joueur=Joueur(AI_1,'Noir',True,self.AI_type[0])
        joueur_restant=Joueur(AI_2,'Blanc',True,self.AI_type[0])
        self.addJoueur(new_joueur)
        self.addJoueur(joueur_restant)

    def addJoueur(self,joueur):
        if joueur.couleur=='Noir':
            self.listeJoueurs[0]=joueur
        else:
            self.listeJoueurs[1]=joueur

    def tourJoueur(self,joueur):
        coup_pas_possible=self.board.checkBoardsolved(joueur.couleur)
        if not coup_pas_possible:
            if not joueur.AI:
                tour_valide=False
                while not tour_valide:
                    print(f"Joueur {joueur.nom} {joueur.couleur}: A toi de jouer")
                    print("Ligne :")
                    row=int(input())
                    print("Colonne :")
                    col=int(input())
                    tour_valide = self.board.placePion((row-1,col-1), joueur.couleur)
            else:
                row,col=joueur.Choice(self.board)
                self.board.placePion((row,col), joueur.couleur)
        return coup_pas_possible
    
    def partie(self,afficher=True):
        tour=0
        self.board.printBoard(afficher)
        tour_sans_coups=0
        while tour_sans_coups<2:
            joueur_actuel=self.detJoueur(tour)
            self.board.printBoard(afficher)
            coup_pas_possible = self.tourJoueur(joueur_actuel)
            if coup_pas_possible:
                tour_sans_coups +=1
            else:
                tour_sans_coups = 0
            tour += 1
        sc_black,sc_white = self.finPartie(afficher)
        return self.board.score_black,self.board.score_white

            
    def detJoueur(self,tour):
        if tour%2==0:
            return self.listeJoueurs[0]
        else:
            return self.listeJoueurs[1]
        
    # def checkFinDePartie(self,joueur):
    #     self.findepartie=self.board.checkBoardsolved(joueur.couleur)
        
    def finPartie(self,afficher):
        self.board.score()
        if not afficher:
            return self.board.score_black,self.board.score_white
        else:
            self.board.printBoard()
            print("Fin de la Partie")
            print(f"Score Noir : {self.board.score_black}")
            print(f"Score Blanc : {self.board.score_white}")
            return self.board.score_black,self.board.score_white

        
# partie=Partie()
# partie.menu()