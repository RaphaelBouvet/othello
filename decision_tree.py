#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:44:00 2022

@author: raphael.bouvet@Digital-Grenoble.local
"""

class DecisionTree:
    
    def __init__(self,board,parent=None,name='First',depth=4,choix_ini=0):
        self.board=board
        self.children=[]
        self.depth=depth
        self.name=name
        self.parent=parent
        self.choix_ini= str(choix_ini)
        self.addNode()
        
        
    