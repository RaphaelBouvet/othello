#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:55:55 2022
"""

from play import Partie
import matplotlib.pyplot as plt


class Manager:
    
    def menu(self):
        print("========== Othello version 3 ========")
        print("a) Mode JvsJ")
        print("b) Vs AI")
        print("c) Mode auto AI vs AI (random vs random)")
        print("d) Simulation AI vs AI")
        choix=input('Choix : ')
        if choix =='a':
            partie=Partie(2)
            partie.partie()
        elif choix =='b':
            AI_type = self.subMenuVsOrdi()
            partie=Partie(1,AI_type)
            partie.partie()
        elif choix =='c':
            AI_1=self.subMenuVsOrdi()
            AI_2=self.subMenuVsOrdi()
            partie=Partie(0,(AI_1,AI_2))
            partie.partie()
        elif choix=='d':
            nb_simul=int(input("Nombre de simulations: "))
            AI_1=self.subMenuVsOrdi()
            AI_2=self.subMenuVsOrdi()
            self.simulationAiVsAi(nb_simul,AI_1,AI_2)
        else:
            exit()
    
    def subMenuVsOrdi(self):
        print("============ Ordinateur ==========")
        print("Choisir une difficulée d'algorythme:")
        print("a) Meilleur Choix_v1")
        print("b) Choix aléatoire (par defaut)")
        choix=input('Choix : ')
        AI_type="random"
        if choix =='a':
            AI_type="v1"
        elif choix=='b':
            AI_type="random"
        return AI_type 
    
    def simulationAiVsAi(self,nb_simul,AI_1,AI_2):
        score_AI_1=0
        score_AI_2=0
        middle=round(nb_simul/2)
        for i in range(0,middle):
            partie=Partie(0,(AI_1,AI_2))
            s_1,s_2=partie.partie(True)
            score_AI_1 += s_1
            score_AI_2 += s_2
        for i in range(middle,nb_simul):
            partie=Partie(0,(AI_1,AI_2))
            s_1,s_2=partie.partie(True)
            score_AI_1 += s_1
            score_AI_2 += s_2
        print(f"Pour l'algo {AI_1} : score moyen {score_AI_1/nb_simul}")
        print(f"Pour l'algo {AI_2} : score moyen {score_AI_2/nb_simul}")
                
manager=Manager()         
manager.menu()