# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 08:45:38 2020

@author: lalai
"""

class Point3D:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return "("+str(self.x)+" ; "+str(self.y)+" ; "+str(self.z)+")"
    
    def module(self):
        return(self.x**2+self.y**2+self.z**2)**0.5
        
    def __add__(self,v):
        return Point3D(self.x+v.x,self.y+v.y,self.z+v.z)
    
    def __sub__(self,v):
        return Point3D(self.x-v.x,self.y-v.y,self.z-v.z)
    
    def __eq__(self,v):
        return self.x==v.x and self.y==v.y and self.z==v.z
    
    def __mul__(self,v):
        if isinstance(v,Point3D):
            return self.x*v.x+self.y*v.y+self.z*v.z
        elif isinstance(v,int) or (v,float):
            return Point3D(v*self.x,v*self.y,v*self.z)
    
    def __matmul__(self,v):
        return Point3D(self.y*v.z-self.z*v.y,self.z*v.x-self.x*v.z,self.x*v.y-self.y*v.z)
    
    def __setitem__(self,i,a):
        if i==0:
            self.x=a
        if i==1:
            self.y=a
        else:
            self.z=a
        
    def __getitem__(self,i):
        a=0
        if i==0:
            a=self.x
        if i==1:
            a=self.y
        else:
            a=self.z
        return a
    
#________________________________________________________
        
class Mass3D(Point3D):
    def __init__(self,x,y,z,m):
        Point3D.__init__(self,x,y,z)
        self.m=m
    def __str__(self):
        return "coordonnées = "+Point3D.__str__()+"; masse = "+str(self.m)
        
    def __setitem__(self,i,a):
        if i==0:
            self.v=a
        else:
            self.m=a
    
    def __getitem__(self,i):
        if i==0:
            return self.v
        else:
            return self.m

#_________________________________________________________

Semestre2={'janvier':31,'février':29,'mars':31,'avril':30,'mai':31,'juin':30}

print(Semestre2.keys())
print(Semestre2.values())
Mois=Semestre2.keys()
Jours=Semestre2.values()

        
def Exo1():
    fsource=open(r"nombrereel.txt","r")
    fdest=open(r"nombrereeldest.txt","w")
    for l in fsource:
        fdest.write(str(round(float(l)))+"\n")
    fdest.close()
    fsource.close()


"""Exo1()"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
