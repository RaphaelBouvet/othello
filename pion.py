#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:59:28 2022

"""

from color import Color

class Pion:
    def __init__(self,position,couleur=None):
        self.position=position
        self.couleur=couleur
        
    def retourner(self):
        if self.couleur=='Noir':
            self.couleur='Blanc'
        elif self.couleur=='Blanc':
            self.couleur='Noir'
        
    def show(self):
        if self.couleur==None:
            output = "." 
        elif self.couleur=='Noir':
            output = Color.BLACK +"0" + Color.END
        else :
            output = Color.WHITE +"0" + Color.END
        return output
    
    def changeColor(self,new_couleur):
        self.couleur=new_couleur



