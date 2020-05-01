# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:20:55 2020

@author: 33664
"""

##Exo1
#def Exo1():
#    f = open(r'C:\Users\33664\nombre.txt','r')
#    farrondi = open(r'C:\Users\33664\nombrearrondi.txt','w')
#    for line in f:
#        line = line.upper()
#        arrondi = round(float(line))
#        farrondi.write(str(arrondi) + "\n")
#    f.close()
#    farrondi.close()

##Exo2
#def bissextile(annee):
#    bissextile = False
#    if(annee % 4 == 0):
#        if(annee % 400 == 0):
#            bissextile = True
#        elif(annee % 100 == 0):
#            bissextile = False
#        else:
#            bissextile = True
#    print("l'année est bissextile: ",bissextile)
#    return bissextile
#def Exo2(annee):
#    semestre2 = {"janvier":31,"février":28,"mars":31,"avril":30,"mai":31,"juin":30}
#  
#    if(bissextile(annee)):
#        semestre2["février"] = 29
#    print("les clés: ",list(semestre2.keys()))
#    print("les valeurs: ",list(semestre2.values()))
#    
#    semestre1 = {'septembre':27,'octobre':31,'novembre':30,'décembre':31}
#    anneeScolaire = {}
#    anneeScolaire.update(semestre1)
#    anneeScolaire.update(semestre2)
#    print(anneeScolaire)
#    vacanceScolaire = {}
#    
#Exo2(2020)

##Exo3
import math
class Point3D:
    def __init__(self,x = 0.0,y = 0.0,z = 0.0):
        self.x=x
        self.y=y
        self.z=z
        print("point instancié")
    def __str__(self):
        return "x: " + str(self.x) + "\ny: " + str(self.y) + "\nz: " + str(self.z)
        #return "(%.3f, %.3f, %.3f)" %(self.x,self.y,self.z) # %.3f -> 3 chiffres après la virgule pour self.x
    def module(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    def __add__(self,v):
        vFinal = Point3D(self.x + v.x,self.y + v.y,self.z + v.z)
        return vFinal
    def __mul__(self,s):
        if isinstance(s,Point3D):
            return self.x * s.x + self.y * s.y + self.z * s.z
        elif(isinstance(s,int) or isinstance(s,float)):
            return Point3D(self.x * s,self.y * s,self.z * s)
    def __getitem__(self,i): #pour obtenir la ième coordonnées d'un p : p[i]
        assert i in range(3) #vérifie qu'on rentre une valeur entre 0 et 3 exclus
        if (i == 0):
            return self.x
        if (i == 1):
            return self.y
        if (i == 2):
            return self.z
        
#class Mass3D(Point3D):
#    def __init__(self,x,y,z,m = 0):
#        Point3D.__init__(self,x,y,z)
#        self.m = m
#        print("point instancié")
#    def __str__(self):
#        return Point3D.__str__(self) + "\nmasse: "  + str(self.m)
#    p = Mass3D(1,2,3,4)
#    print(p)
#    
    
  