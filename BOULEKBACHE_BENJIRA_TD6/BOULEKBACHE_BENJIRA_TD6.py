# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:22:43 2020

@author: 33664
"""
from tkinter import *
import numpy as np
import pickle

class Vect4D:
    def __init__(self,x,y,z,t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
    def __setitem__(self,i,valeur):
        assert i in range(4)
        if(i == 0):
            self.x = valeur
        elif(i == 1):
            self.y = valeur
        elif(i == 2):
            self.z = valeur
        else:
            self.t = valeur
    def __getitem__(self,i):
        assert i in range(4)
        if(i == 0):
            return self.x
        elif(i == 1):
            return self.y
        elif(i == 2):
            return self.z
        else:
            return self.t
    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+', '+str(self.z)+', '+str(self.t)+')'
    def module(self):
        return 'module: '+ ( (self.x)**2 + (self.y)**2 + (self.z)**2 + (self.t)**2 )**0.5
    def __add__(self,v):
        return Vect4D(self.x + v.x, self.y + v.y, self.z + v.z, self.t + v.t)
    def __sub__(self,v):
        return Vect4D(self.x - v.x, self.y - v.y, self.z - v.z, self.t - v.t) 
    def __bool__(self,v):
        res = False
        if(self.x == v.x and self.y == v.y and self.z == v.z and self.t == v.t):
            res = True
        return res
    def __mul__(self, v):
        if(type(v) == float or type(v) == int):
            return Vect4D(self.x * v, self.y * v,self.z * v, self.t * v)
        elif(type(v) == Vect4D):
            return self.x * v.x +self.y * v.y + self.z * v.z + self.t * v.t
        else:
            return 'erreur'
    


class Mat4D:
    def __init__(self,v1 = None,v2 = None, v3 = None, v4 = None):
        if(v1 == None and v2 == None and v3 == None and v4 == None):
            input("création matrice: \n")
            v1_0 = int(input("v1[0]: "))
            v1_1 = int(input("v1[1]: "))
            v1_2 = int(input("v1[2]: "))
            v1_3 = int(input("v1[3]: "))
            v1 = Vect4D(v1_0,v1_1,v1_2,v1_3)
            v2_0 = int(input("v2[0]: "))
            v2_1 = int(input("v2[1]: "))
            v2_2 = int(input("v2[2]: "))
            v2_3 = int(input("v2[3]: "))
            v2 = Vect4D(v2_0,v2_1,v2_2,v2_3)
            v3_0 = int(input("v3[0]: "))
            v3_1 = int(input("v3[1]: "))
            v3_2 = int(input("v3[2]: "))
            v3_3 = int(input("v3[3]: "))
            v3 = Vect4D(v3_0,v3_1,v3_2,v3_3)
            v4_0 = int(input("v4[0]: "))
            v4_1 = int(input("v4[1]: "))
            v4_2 = int(input("v4[2]: "))
            v4_3 = int(input("v4[3]: "))
            v4 = Vect4D(v4_0,v4_1,v4_2,v4_3)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
       
    def __str__(self):
        mat = ""
        mat = mat +  "(" + str(self.v1.x) + " " + str(self.v2.x) + " " + str(self.v3.x) + " " + str(self.v4.x) + ")" + "\n"
        mat = mat +  "(" + str(self.v1.y)+ " " + str(self.v2.y) + " " + str(self.v3.y) + " " + str(self.v4.y) + ")" + "\n"
        mat = mat +  "(" + str(self.v1.z) + " " + str(self.v2.z) + " " + str(self.v3.z) + " " + str(self.v4.z) + ")" + "\n"
        mat = mat +  "(" + str(self.v1.t) + " " + str(self.v2.t) + " " + str(self.v3.t) + " " + str(self.v4.t) + ")" + "\n"
        return mat
    def __add__(self,m):
        return Mat4D(self.v1 + m.v1 , self.v2 + m.v2, self.v3 + m.v3 , self.v4 + m.v4)
    def __sub__(self,m):
        assert type(m) == Mat4D
        return Mat4D(self.v1 - m.v1, self.v2 - m.v2, self.v3 - m.v3, self.v4 - m.v4) 
    def __bool__(self,m):
        assert type(m) == Mat4D
        res = False
        if(self.v1 == m.v1 and self.v2 == m.v2 and self.v3 == m.v3 and self.v4 == m.v4):
            res = True
        return res
    def __mul__(self, m):
        if(type(m) == float or type(m) == int):
            return Mat4D(self.v1 * m, self.v2 * m, self.v3 * m, self.v4 * m)
        elif(type(m) == Vect4D):
            v_1 = Vect4D(self.v1.x, self.v2.x, self.v3.x, self.v4.x) #on crée des vecteurs lignes pour faciliter la multiplication car les vecteurs de Vect4D des vecteurs colonnes
            v_2 = Vect4D(self.v1.y, self.v2.y, self.v3.y, self.v4.y)
            v_3 = Vect4D(self.v1.z, self.v2.z, self.v3.z, self.v4.z)
            v_4 = Vect4D(self.v1.t, self.v2.t, self.v3.t, self.v4.t)
            return Vect4D(m * v_1, m * v_2, m * v_3, m * v_4)
        elif(type(m) == Mat4D):
            l1c1 = self.v1.x * m.v1.x + self.v2.x * m.v1.y + self.v3.x * m.v1.z + self.v4.x * m.v1.t
            l1c2 = self.v1.x * m.v2.x + self.v2.x * m.v2.y + self.v3.x * m.v2.z + self.v4.x * m.v2.t
            l1c3 = self.v1.x * m.v3.x + self.v2.x * m.v3.y + self.v3.x * m.v3.z + self.v4.x * m.v3.t
            l1c4 = self.v1.x * m.v4.x + self.v2.x * m.v4.y + self.v3.x * m.v4.z + self.v4.x * m.v4.t
            l2c1 = self.v1.y * m.v1.x + self.v2.y * m.v1.y + self.v3.y * m.v1.z + self.v4.y * m.v1.t
            l2c2 = self.v1.y * m.v2.x + self.v2.y * m.v2.y + self.v3.y * m.v2.z + self.v4.y * m.v2.t
            l2c3 = self.v1.y * m.v3.x + self.v2.y * m.v3.y + self.v3.y * m.v3.z + self.v4.y * m.v3.t
            l2c4 = self.v1.y * m.v4.x + self.v2.y * m.v4.y + self.v3.y * m.v4.z + self.v4.y * m.v4.t
            l3c1 = self.v1.z * m.v1.x + self.v2.z * m.v1.y + self.v3.z * m.v1.z + self.v4.z * m.v1.t
            l3c2 = self.v1.z * m.v2.x + self.v2.z * m.v2.y + self.v3.z * m.v2.z + self.v4.z * m.v2.t
            l3c3 = self.v1.z * m.v3.x + self.v2.z * m.v3.y + self.v3.z * m.v3.z + self.v4.z * m.v3.t
            l3c4 = self.v1.z * m.v4.x + self.v2.z * m.v4.y + self.v3.z * m.v4.z + self.v4.z * m.v4.t
            l4c1 = self.v1.t * m.v1.x + self.v2.t * m.v1.y + self.v3.t * m.v1.z + self.v4.t * m.v1.t
            l4c2 = self.v1.t * m.v2.x + self.v2.t * m.v2.y + self.v3.t * m.v2.z + self.v4.t * m.v2.t
            l4c3 = self.v1.t * m.v3.x + self.v2.t * m.v3.y + self.v3.t * m.v3.z + self.v4.t * m.v3.t
            l4c4 = self.v1.t * m.v4.x + self.v2.t * m.v4.y + self.v3.t * m.v4.z + self.v4.t * m.v4.t
            v1 = Vect4D(l1c1, l2c1, l3c1, l4c1)     #Vecteur colonne 1
            v2 = Vect4D(l1c2, l2c2, l3c2, l4c2)    #Vecteur colonne 2
            v3 = Vect4D(l1c3, l2c3, l3c3, l4c3)     #Vecteur colonne 3
            v4 = Vect4D(l1c4, l2c4, l3c4, l4c4)    #Vecteur colonne 4   
            return Mat4D(v1,v2,v3,v4)#                    
        else:
            return 'erreur'
    def __setitem__(self,i,j,valeur):
        assert i in range(4)
        assert j in range(4)
        if(i == 0):
            self.v1[j] = valeur
        elif(i == 1):
            self.v2[j] = valeur
        elif(i == 2):
            self.v3[i] = valeur
        elif(i == 3):
            self.v3[j] = valeur
    def __getitem__(self,i,j):
        assert i in range(4)
        assert j in range(4)
        if(i == 0):
            return self.v1[j]
        elif(i == 1):
            return self.v2[j]
        elif(i == 2):
            return self.v3[j]
        else:
            return self.v4[j]
   
    
def Id4():
    return Mat4D( (1,0,0,0) , (0,1,0,0) , (0,0,1,0) , (0,0,0,1) )
#symétrie
def SymX():
    return Mat4D(Vect4D(-1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))
def SymY():
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, -1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))
def SymZ():
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, -1, 0), Vect4D(0, 0, 0, 1))
#translation
def TransX(a):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(a, 0, 0, 1))
def TransY(a):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, a, 0, 1))
def TransZ(a):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, a, 1))
#rotation
def RotX(theta):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, np.cos(theta), -np.sin(theta), 0), Vect4D(0, np.sin(theta), np.cos(theta), 0), Vect4D(0, 0, 0, 1))
def RotY(theta):
    return Mat4D(Vect4D(np.cos(theta), 0, -np.sin(theta), 0), Vect4D(0, 1, 0, 0), Vect4D(np.sin(theta), 0, np.cos(theta), 0), Vect4D(0, 0, 0, 1))
def RotZ(theta):
    return Mat4D(Vect4D(np.cos(theta), -np.sin(theta), 0, 0), Vect4D(np.sin(theta), np.cos(theta), 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))
    

    


#if __name__ == __main__:
#    Id4()
window = Tk()
window.title("Transformation d'une matrice") 
window.geometry("1080x720")
window.config(background = 'beige')



##  FRAME QUI CONTIENT LE TITRE
frame_text = Frame(window,bg='beige',bd=1,relief=SUNKEN)
frame_text.pack(padx=40,fill=X)


#  titre de la fenêtre
label_title = Label(frame_text,text="Transformation d'une matrice", font=('Arial',35),bg='beige',fg='black')
label_title.pack(pady=5)



label_coord = Label(window,text="Saisissez les coordonnées:", font=('Arial',20),bg='beige',fg='black')
label_coord.pack()

##  FRAME QUI CONTIENT LES BOUTONS
frame_mat = Frame(window,bg='beige',bd=1,relief=SUNKEN)
frame_mat.pack(padx=352.5,pady=15,fill=X)

frame_calcul = Frame(window,bg='beige',bd=1,relief=SUNKEN)
frame_calcul.pack(padx=352.5,pady=40)


# l'utilisateur entre les coordonnées à transformer

x = Label(frame_mat,text="X:", font=('Arial',20),bg='beige',fg='black')
x.grid(row=0,column=0)
y = Label(frame_mat,text="Y:", font=('Arial',20),bg='beige',fg='black')
y.grid(row=0,column=1)
z = Label(frame_mat,text="Z:", font=('Arial',20),bg='beige',fg='black')
z.grid(row=0,column=2)


x_entry = Entry(frame_mat,bg='beige',fg='black')
x_entry.grid(row=1,column=0,sticky='ew',ipady=10)
y_entry = Entry(frame_mat,bg='beige',fg='black')
y_entry.grid(row=1,column=1,sticky='ew',ipady=10)
z_entry = Entry(frame_mat,bg='beige',fg='black')
z_entry.grid(row=1,column=2,sticky='ew',ipady=10)




# l'utilisateur saisit les variables de transformation

label_title2 = Label(window,text="Saisissez les variables:", font=('Arial',20),bg='beige',fg='black')
label_title2.place(x=400,y=210)
theta1 = Label(frame_calcul,text="Theta1: \n(rotation autour de l'axe X)", font=('Arial',15),bg='beige',fg='black')
theta1.grid(row=1,column=0)
theta2 = Label(frame_calcul,text="Theta2: \n(rotation autour de l'axe Y)", font=('Arial',15),bg='beige',fg='black')
theta2.grid(row=2,column=0)
theta3 = Label(frame_calcul,text="Theta3: \n(rotation autour de l'axe X)", font=('Arial',15),bg='beige',fg='black')
theta3.grid(row=3,column=0)
theta4 = Label(frame_calcul,text="Theta4: \n(rotation autour de l'axe Z)", font=('Arial',15),bg='beige',fg='black')
theta4.grid(row=4,column=0)
l = Label(frame_calcul,text="L: \n(translation le long de l'axe X)", font=('Arial',15),bg='beige',fg='black')
l.grid(row=5,column=0)
theta1_e = Entry(frame_calcul,bg='beige',fg='black')
theta1_e.grid(row=1,column=1,sticky='nesw')
theta2_e = Entry(frame_calcul,bg='beige',fg='black')
theta2_e.grid(row=2,column=1,sticky='nesw')
theta3_e = Entry(frame_calcul,bg='beige',fg='black')
theta3_e.grid(row=3,column=1,sticky='nesw')
theta4_e = Entry(frame_calcul,bg='beige',fg='black')
theta4_e.grid(row=4,column=1,sticky='nesw')
L_e = Entry(frame_calcul,bg='beige',fg='black')
L_e.grid(row=5,column=1,sticky='nesw')

def valider():
    M1 = RotX(float(theta1_e.get())/180 * np.pi) #en rad
    M2 = RotY(float(theta2_e.get())/180 * np.pi)
    M3 = RotX(float(theta3_e.get())/180 * np.pi)
    M4 = RotZ(float(theta4_e.get())/180 * np.pi)
    L = TransX(float(L_e.get()))
    M = M1 * M2 * M3 * M4 * L
    matricetxt.set(str(M) + "\n\n")
    V = Vect4D(float(x_entry.get()), float(y_entry.get()), float(z_entry.get()), 1)
    vecteurtxt.set("(" + str(abs((M*V).x)) + ", " + str(abs((M*V).y)) + ", " + str(abs((M*V).z)) + ", " + str(abs((M*V).t)) + ")\n\n\n\n")

matricetxt = StringVar()
matricetxt.set("(0.0, 0.0, 0.0, 0.0)\n(0.0, 0.0, 0.0, 0.0)\n(0.0, 0.0, 0.0, 0.0)\n(0.0, 0.0, 0.0, 0.0)\n\n")
vecteurtxt = StringVar()
vecteurtxt.set("(0, 0, 0, 0)\n\n\n\n")

mat = Label(window, textvariable = matricetxt,font=('Arial',15),bg='beige',fg='black')
mat.pack(expand=YES,side=RIGHT)
mat_text = Label(window, text = 'Matrice',font=('Arial',15),bg='beige',fg='black')
mat_text.place(x=760,y=670)

vect = Label(window, textvariable = vecteurtxt,font=('Arial',15),bg='beige',fg='black')
vect.pack(expand=YES,side=LEFT)
vect_text = Label(window, text = 'Vecteur en coordonnées absolues',font=('Arial',15),bg='beige',fg='black')
vect_text.place(x=100,y=620)


valid = Button(window,text='Valider',font=('Arial',15),bg='black',fg='beige',command=valider)
valid.place(height=50,x=500,y=600)



window.mainloop()



