# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:19:31 2020

@author: 33664
"""

#MUTABLE :  tab[] list  dict set
#NON MUTABLE : string tuple

## EXO2
import random

class Individu:
    def __init__(self, val=None):
        if val == None:
            self.val= random.sample(range(8),8)
        else:
            self.val = val
    def __str__(self):
        return " ".join([str(i) for i in self.val]) #qlq soit i appartenant à la liste
    
    i = Individu()
    print(i)
    
    def conflict(p1,p2):
        '''retourne true si la reine à la position p1 est en conflit avec la reine en position p2'''
        return p1[0] == p2[0] or p1[1] == p2[1] or abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])
              #même ligne           même colonne       même diagonale