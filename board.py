#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:01:33 2022

"""

from pion import Pion
from color import Color
import os

class Board:
    def __init__(self):
        self.arr=[["." for col in range(8)] for row in range(8)]
        for i,row in enumerate(self.arr):
            for j,col in enumerate(row):
                self.arr[i][j]=Pion((i,j))
        self.score_black=0
        self.score_white=0
        
    def printBoard(self):
        os.system("clear")
        f_line='  1 2 3 4 5 6 7 8'
        print(f_line)
        for i,row in enumerate(self.arr):
            line ="" + str(i+1)+ " "
            for j,pion in enumerate(row):
                line += pion.show() + " "
            print(line)
                
    def placePion(self,position,couleur,start=False):
        row=position[0]
        col=position[1]
        if start:
            self.arr[row][col].changeColor(couleur)
        else:
            is_valid,liste_retournement=self.valide_position(position,couleur)
            if is_valid:
                self.arr[row][col].changeColor(couleur)
                for position in liste_retournement:
                    self.arr[position[0]][position[1]].retourner()
                return True
            else:
                return False
                
    def valide_position(self,position,couleur):
        row=position[0]
        col=position[1]
        if not row in range(8) or not col in range(8): # mauvais indice
            print(f"{Color.RED} Mauvaise position (Indices) Merci de rentrer des positions valides {Color.END}")
            return False,None
        elif self.arr[row][col].couleur!=None: # sur pion existant
            print(f"{Color.RED} Mauvaise position (Pion existant): Merci de rentrer des positions valides {Color.END}")
            return False,None
        elif not self.findVoisinOppose(position,couleur): #pas de voisin de couleur oppoée
            print(f"{Color.RED} Mauvaise position (Pas adjacent à opposant): Merci de rentrer des positions valides {Color.END}")
            return False,None
        else:
            retournement_possible,liste_retournement = self.retournementPossible(position,couleur)
            if not retournement_possible:
                print(f"{Color.RED} Mauvaise position (Pas de retournement): Merci de rentrer des positions valides {Color.END}")
                return False,None
            else:
                return True,liste_retournement
            
    def valide_position_ai(self,position,couleur):
        row=position[0]
        col=position[1]
        if not row in range(8) or not col in range(8): # mauvais indice
            return False,None
        elif self.arr[row][col].couleur!=None: # sur pion existant
            return False,None
        elif not self.findVoisinOppose(position,couleur): #pas de voisin de couleur oppoée
            return False,None
        else:
            retournement_possible,liste_retournement = self.retournementPossible(position,couleur)
            if not retournement_possible:
                return False,None
            else:
                return True,liste_retournement

    def findVoisinOppose(self,position,couleur):
        liste_voisin=[]
        liste_row=[x for x in range(position[0]-1,position[0]+2)]
        liste_col=[x for x in range(position[1]-1,position[1]+2)]
        for row,col in [(row,col) for row in liste_row for col in liste_col]:
            if row in range(8) and col in range(8):
                liste_voisin.append(self.arr[row][col])
        liste_voisin.remove(self.arr[position[0]][position[1]])
        is_different=False
        for voisin in liste_voisin:
            if voisin.couleur!=couleur and voisin.couleur!=None:
                is_different=True
        print(is_different)
        return is_different
    
    def retournementPossible(self,position,couleur):
        
        
        liste_retournement=[]
        row_ini=position[0]
        col_ini=position[1]
        
        right=[(row_ini,col) for col in range(col_ini+1,8)] #right
        left=[(row_ini,col) for col in range(col_ini-1,-1,-1)] #left
        up=[(row,col_ini) for row in range(row_ini-1,-1,-1)] #up
        down=[(row,col_ini) for row in range(row_ini+1,8)] #down
        down_right=[(row,col) for row,col in zip(range(row_ini+1,8),range(col_ini+1,8))] #down_right
        up_right=[(row,col) for row,col in zip(range(row_ini-1,-1,-1),range(col_ini+1,8))] #up_right
        up_left=[(row,col) for row,col in zip(range(row_ini-1,-1,-1),range(col_ini-1,-1,-1))] #up_left
        down_left=[(row,col) for row,col in zip(range(row_ini+1,8),range(col_ini-1,-1,-1))] #down_left
        liste_direction_pos=[right,left,up,down,down_right,up_right,up_left,down_left]
        liste_pion_verifier=[]
        
        for direction in liste_direction_pos:
            direction_pion=[]
            for position in direction:
                row=position[0]
                col=position[1]
                direction_pion.append(self.arr[row][col])
            liste_pion_verifier.append(direction_pion)
            
        for direction in liste_pion_verifier:
            first_opposite=False
            found_same=False
            for i,pion in enumerate(direction):
                if i==0 and pion.couleur!=couleur and pion.couleur!=None:
                    first_opposite=True
                if i>0 and pion.couleur==couleur:
                    found_same=True
            if first_opposite and found_same:
                for pion in direction:
                    if pion.couleur==None or pion.couleur==couleur:
                        break
                    else:
                        liste_retournement.append(pion.position)
                    
        if len(liste_retournement)==0:
            return False,None
        else: 
            return True, liste_retournement
        
    def findPion(self,position):
        row=position[0]
        col=position[1]
        return self.arr[row][col]
    
    def checkBoardsolved(self,couleur_joueur):
        placement_possible=False
        for row in self.arr:
            for pion in row:
                placement_possible,__= self.valide_position_ai(pion.position,couleur_joueur)
                if placement_possible:
                    return False
        return True
    
    def score(self):
        self.score_black=0
        self.score_white=0
        for row in self.arr:
            for pion in row:
                if pion.couleur=='Noir':
                    self.score_black += 1
                elif pion.couleur=='Blanc':
                    self.score_white += 1