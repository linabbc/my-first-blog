# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:31:00 2020

@author: 33664
"""
##EXO2
" ".join( [ str(x*7) + ("*" if x * 7 % 3 ==0 else "")  for x in range(1,21)])



##EXO3
import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1,2,3,4],[1,4,2,3])
#plt.show()

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()



##EXO4

# LES CONDITIONS INITIALES DE LA SIMULATION

p0 = np.array([0.,0.,0.]) # position initiale de l'extremiré fixe du ressort
p1 = np.array([0.,-1.,0.]) #position au repos de l'extremite libre du ressort
m = 1 # m est la masse de l'extremite libre
k = 0.1 #raideur du ressort
amort = 0.1 #ammortissement du ressort
delta = 1.0 #pas de l'intégration
time_sim = 50 #durée de la simulation

acc = np.array([0.,0.,0.])
at = np.arrange(0,time_sim,delta) #vecteur temps de la simulation allant de 0 à time_sim avec un pas de delta
longueur_0 = np.sqrt = np.sqrt(np.dot(p1 - p0,p1 - p0)) #longueur initiale = norme du vecteur P1P0
v = np.array([0.,0.,0.]) #vitesse 
longueur = np.sqrt(np.dot(p1 - p0,p1 - p0)) 
deltalong = longueur - longueur_0