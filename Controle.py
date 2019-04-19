# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:53:51 2019

@author: Villebon
"""
#mon_fichier = open("marine.txt","r",encoding="latin")
#Mot = mon_fichier.read()
#print(Mot) d j

fichier = open("marine.txt","r", encoding="latin")
Mot=fichier.read()
#fichier.close()
Taille=len(Mot)
Chiffre=0 #Variable qui représente la valeur de la lettre dans le dic pointé par i
Decal=0 #Variable qui va servir à changer la valeur de la lettre 
Dic={} #Création de dictionnaires pour les 2 clés
Dic2={} #Création de dictionnaires pour les 2 clés
Borne=0 #Variable trouver grâce au dic
d=0 #Variable pour les boucles
C=0
L=0
e=0 #Variable pour les boucles

# Code pour séparer les Dic en 2 parties (d'un côté les pairs et l'autres les impairs)
for c in Mot:
    d=d+1
    if d % 2 == 0 :
        if c in Dic:
            Dic[c]=Dic[c]+1
        else:
            Dic[c]=1
    else:
        if c in Dic2:
            Dic2[c]=Dic2[c]+1
        else:
            Dic2[c]=1
print(Dic)
      
for x in Dic:   
    print (x,':',Dic[x])
    
print("-----------------------------------")

for y in Dic2:   
    print (y,':',Dic2[y])    
#-------------------------------

L=ord('h')
print(L)
C=ord('c')
Borne= L-C
print(Borne)

L=ord('#')
print(L)
C=ord(' ')
Borne2= L-C
print(Borne2)
Nouv=""

for i in range(Taille):#Sépare le tri en 2 parties et que chaque borne agis sur une partie
               #différente
    if i%2==0:
        Chiffre=ord(Mot[i])
        Decal=chr(Chiffre-Borne)
        Nouv=Nouv+Decal
    else:
        Chiffre=ord(Mot[i])
        Decal=chr(Chiffre-Borne2)
        Nouv=Nouv+Decal
#fichier = open("Marine_dechiffre.txt", "w", encoding="latin")
#fichier.write(Nouv)
#fichier.close()
print(Nouv[:20])