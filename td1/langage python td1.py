# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""
def Exo0():
    print("voila l'exo zero")
    
if __name__=='__main__':
    Exo0()
"""

#1
def Exo1():
    temps=6.892
    distance=19.7
    vitesse=distance/temps
    return round(vitesse,1)
print(Exo1())
    
def Exo2b(a,b):
    mini=a
    maxi=b
    if(mini>maxi):
        inter=mini
        mini=maxi
        maxi=inter
    return mini,maxi
print(Exo2b(5,3))

def Exo2a(a,b):
    mini=min(a,b)
    maxi=max(a,b)
    return mini,maxi
print(Exo2a(6,4))

#3
def volBoite(x1=-1,x2=-1,x3=-1):
    if(x1==-1 and x2==-1 and x3==-1):
        return -1    #erreur
    elif(x2==-1 and x3==-1):
        return x1**3 #cube
    elif(x3==-1):
        return x2*(x1**2) #prisme à base carrée
    else:
        return x1*x2*x3 #para

print(volBoite()) #erreur
print(volBoite(5.2)) #cube
print(volBoite(5.2,3)) #prisme à base carrée
print(volBoite(5.2,3,7.4)) #parallelepipede

def eleMax(liste,debut=0,fin=-1):
    if (fin == -1):
        fin=len(liste)
    maxi=liste[debut]
    for i in range(debut,fin):
        if(maxi<liste[i]):
            maxi=liste[i]
    return maxi

serie=[9,3,6,1,7,5,4,8,2]
print(eleMax(serie))
print(eleMax(serie,2,5))
print(eleMax(serie,2))
print(eleMax(serie,fin=3,debut=1))
   
#5
def Liste( t1 , t2 ):
    n = len(t1) + len(t2)
    t3 = [0] * n
    for i in range(len(t3)):
        if(i%2 == 0): #indice pair -> liste des mois
            t3[i] = t2[i//2]
        else:         #indice impair -> liste des jours
            t3[i] = t1[i//2] 
    return t3

t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
print(Liste(t1,t2))

#6
def Retourne(mot):
    


