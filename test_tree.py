#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:31:18 2022

@author: raphael.bouvet@Digital-Grenoble.local
"""

liste_valeurs=[]

class Dtree:
        
    def __init__(self,board,parent=None,name='Papa',depth=4,choix_ini=0):
        self.board=board
        self.children=[]
        self.depth=depth
        self.name=name
        self.parent=parent
        self.choix_ini= str(choix_ini)
        self.addNode()
        

    def addNode(self):
        global liste_valeurs
        if self.depth ==4:
            next_depth=self.depth-1
            liste_position=[i for i in range(3)]
            for i,pos in enumerate(liste_position):
                name=str(next_depth)+"_"+str(i)+"_"+"("+self.name+")"
                new_board=list(self.board)
                new_board[pos] += 1
                self.children.append(Dtree(new_board,self.name,name,next_depth,pos))
        elif self.depth !=0:
            next_depth=self.depth-1
            liste_position=[i for i in range(3)]
            for i,pos in enumerate(liste_position):
                name=str(next_depth)+"_"+str(i)+"_"+"("+self.name+")"
                new_board=list(self.board)
                new_board[pos] += 1
                self.children.append(Dtree(new_board,self.name,name,next_depth,self.choix_ini))
        else:
            liste_valeurs.append((self.recupChoixIni(),self.score()))
    
    def recupChoixIni(self):
        return f"Choix initial : {self.choix_ini}"
    
    def score(self):
        return len(self.board)

                             

liste_ini=[1 for i in range(3)]
tree=Dtree(liste_ini)

