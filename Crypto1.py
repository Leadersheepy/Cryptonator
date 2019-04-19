# -*- coding: utf-8 -*-
"""
"""
    
##-------------------------------------------------
##-------------------------------------------------
#                   TABLEAU
##-------------------------------------------------
##-------------------------------------------------

#-------------------------------------------------
#               MESSAGE 1 VERS1
#-------------------------------------------------
#
fichier = open("message1.txt", encoding="utf-8")
Mot=fichier.read()
#Mot= "JuL dreioVet srom.s dlo "
Taille=len(Mot)
M=int(input('Taille:'))
b = True
for cle in range(2,M):
    Nouv=""
    for i in range(cle):
        for j in range(i,Taille,cle):
            Nouv=Nouv+Mot[j]
#        print(cle)
#        print(Nouv[:15])
    if Nouv[:2]=="Je":
        b = False
        print(Nouv[:15])
        print(cle)

if b:
    print("il n'y a pas :(")
###    
##7
#    
##-------------------------------------------------
##               MESSAGE 1 VERS2
##-------------------------------------------------
#
fichier = open("message1.txt", encoding="utf-8")
Mot=fichier.read()
"""Mot= "JuL dreioVet srom.s dlo""" 

Taille=len(Mot)
M=int(input('Taille:'))
b = True
i=0
Nouv=""
while i<M and Nouv[:14]!= "Fonctionnement":
    for cle in range(2,M):
        for i in range(cle):
            for j in range(i,Taille,cle):
                Nouv=Nouv+Mot[j]
                print(Nouv[:15])
                print(cle)
    
##-------------------------------------------------

#fichier = open("message1.txt", encoding="utf-8")
#Mot=fichier.read()
Mot= "JuL dreioVet srom.s dlo "
Taille=len(Mot)
M=int(input('Taille:'))
b = True
for cle in range(2,M):
    Nouv=""
    for i in range(cle):
        for j in range(i,Taille,cle):
            Nouv=Nouv+Mot[j]
#        print(cle)
#        print(Nouv[:15])
    if Nouv[:2]=="Je":
        b = False
        print(Nouv)
        print(cle)

if b:
    print("il n'y a pas :(")  
    
##-------------------------------------------------
##-------------------------------------------------
#                   CESAR
##-------------------------------------------------
##-------------------------------------------------

 
#
##-------------------------------------------------
##               MESSAGE 2 & 3 Grâce à un mot
##-------------------------------------------------
fichier = open("message2.txt", encoding="utf-8")
Mot=fichier.read()
Mot=""
Taille=len(Mot)
Borne=int(input('Chiffre de César:'))
Chiffre=0 #Variable qui représente la valeur de la lettre dans le dic pointé par i
for decalage in range (Borne):
    Nouv=""
    for i in range(Taille):
        Chiffre=ord(Mot[i])
        Decal=chr(Chiffre-decalage)
        Nouv=Nouv+Decal
    if Nouv[-4:]=="Joël":
        b = False
        print(decalage)
        print(Nouv)  
        
##-------------------------------------------------
##               MESSAGE 2 & 3 sans mot
##-------------------------------------------------
fichier = open("message2.txt", encoding="utf-8")
Mot=fichier.read()
#Mot=""
Taille=len(Mot)
Chiffre=0 #Variable qui représente la valeur de la lettre dans le dic pointé par i
Decal=0 #Variable qui va servir à changer la valeur de la lettre 
Dic={} #Création de dictionnaires pour la clé
Borne=0 #Variable trouver grâce au dic
for c in Mot:
    if c in Dic:
        Dic[c]=Dic[c]+1
    else:
        Dic[c]=1
print(Dic)
#Ici il faudra choisir sur quel lettre vous voulez utiliser comme base pour le code
Lettre=input('Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)

#Ici il faudra choisir en quoi vous voulez transformer la lettre ex: je sais que la derniére
#Lettre sera un l donc je dis à mon programme qu'il doit transformer ma lettre "e" en "l"
Chi=input('Tu veux la transformer en quoi ?:')
C=ord(Chi)

print(C)
Borne= L-C
print(Borne)
Nouv=""
for i in range(Taille):
    Chiffre=ord(Mot[i])
    Decal=chr(Chiffre-Borne)
    Nouv=Nouv+Decal
print(Nouv)


    
##-------------------------------------------------
##-------------------------------------------------
#                   CESAR AVEC 2 CLES
##-------------------------------------------------
##-------------------------------------------------

#
##-------------------------------------------------
##               MESSAGE 4 qui fonctionne mais pas sur spyder
##-------------------------------------------------
##23    
##Mot="""7aĂ"""
fichier = open("message4.txt", encoding="utf-8")
Mot=fichier.read()
#fichier.close()
Taille=len(Mot)
Chiffre=0 #Variable qui représente la valeur de la lettre dans le dic pointé par i
Decal=0 #Variable qui va servir à changer la valeur de la lettre 
Dic={} #Création de dictionnaires pour les 2 clés
Dic2={} #Création de dictionnaires pour les 2 clés
Borne=0 #Variable trouver grâce au dic
d=0 #Variable pour les boucles
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

#Ici il faudra choisir sur quel lettre vous voulez utiliser comme base pour le code
Lettre=input('1-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
#Ici il faudra choisir en quoi vous voulez transformer la lettre ex: je sais que la derniére
#Lettre sera un l donc je dis à mon programme qu'il doit transformer ma lettre "e" en "l"
Chi=input('1-Tu veux la transformer en quoi ?:')
C=ord(Chi)
Borne= L-C
print(Borne)

#Ici il faudra choisir sur quel lettre vous voulez utiliser comme base pour le code
Lettre=input('2-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
#Ici il faudra choisir en quoi vous voulez transformer la lettre ex: je sais que la derniére
#Lettre sera un l donc je dis à mon programme qu'il doit transformer ma lettre "e" en "l"
Chi=input('2-Tu veux la transformer en quoi ?:')
C=ord(Chi)
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
print(Nouv[:20])

    
##-------------------------------------------------
##-------------------------------------------------
#                   CESAR AVEC 3 CLES
##-------------------------------------------------
##-------------------------------------------------
#-------------------------------------------------
#               MESSAGE 5 
#-------------------------------------------------
mon_fichier = open("message5.txt","r",encoding="utf8")
Mot = mon_fichier.read()
#Mot = "Lxîn"
Chiffre=0 #Variable qui représente la valeur de la lettre dans le dic pointé par i
Decal=0 #Variable qui va servir à changer la valeur de la lettre 
Dic1={} #Création de dictionnaires pour les 3 clés
Dic2={} #Création de dictionnaires pour les 3 clés
Dic3={} #Création de dictionnaires pour les 3 clés
d=0 #Variable pour les boucles
f=0 #Variable pour les boucles
g=0 #Variable pour les boucles
e=0 #Variable pour les boucles
#-----------------------------
#Mis en place des 3 Dic
for c in Mot:
    d=d+1
    if d % 3 == 0 :
        if c in Dic3:
            Dic3[c]=Dic3[c]+1
        else:
            Dic3[c]=1
    else:
         f=f+1
         if f % 2 == 0 : 
             if c in Dic2:
                 Dic2[c]=Dic2[c]+1
             else:
                 Dic2[c]=1
         else:
            if c in Dic1:
                 Dic1[c]=Dic1[c]+1
            else:
                 Dic1[c]=1
print(Dic1)
      
for x in Dic1:   
    print (x,':',Dic1[x])
    
print("-----------------------------------")

for y in Dic2:   
    print (y,':',Dic2[y])
    
print("-----------------------------------")

for z in Dic3:   
    print (z,':',Dic3[z])
#-----------------------------
 
#Ici il faudra choisir sur quel lettre vous voulez utiliser comme base pour le code
Lettre=input('1-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
#Ici il faudra choisir en quoi vous voulez transformer la lettre ex: je sais que la derniére
#Lettre sera un l donc je dis à mon programme qu'il doit transformer ma lettre "e" en "l"
Chi=input('1-Tu veux la transformer en quoi ?:')
C=ord(Chi)
Borne= L-C
print(Borne)

#Ici il faudra choisir sur quel lettre vous voulez utiliser comme base pour le code
Lettre=input('2-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
#Ici il faudra choisir en quoi vous voulez transformer la lettre ex: je sais que la derniére
#Lettre sera un l donc je dis à mon programme qu'il doit transformer ma lettre "e" en "l"
Chi=input('2-Tu veux la transformer en quoi ?:')
C=ord(Chi)
Borne2= L-C
print(Borne2)

#Ici il faudra choisir sur quel lettre vous voulez utiliser comme base pour le code
Lettre=input('3-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
#Ici il faudra choisir en quoi vous voulez transformer la lettre ex: je sais que la derniére
#Lettre sera un l donc je dis à mon programme qu'il doit transformer ma lettre "e" en "l"
Chi=input('3-Tu veux la transformer en quoi ?:')
C=ord(Chi)
Borne3= L-C
print(Borne3)
Nouv=""

for i in Mot:
    e=e+1
    if e%3==0: #Code pour séparer le tri en 3 parties et que chaque borne agis sur une partie
               #différente
        Chiffre=ord(i)
        Decal=chr(Chiffre-Borne)
        Nouv=Nouv+Decal
    else:
        g=g+1
        if g%2 ==0:
            Chiffre=ord(i)
            Decal=chr(Chiffre-Borne2)
            Nouv=Nouv+Decal
        else:
            Chiffre=ord(i)
            Decal=chr(Chiffre-Borne3)
            Nouv=Nouv+Decal
print(Nouv)


#-------------------------------------------------
#               MESSAGE 5 TEST 
#-------------------------------------------------

mon_fichier = open("marine.txt","r",encoding="utf8")
Mot = mon_fichier.read()
#Mot = "Lxîn"
Dic1={}
Dic2={}
Dic3={}
d=0
f=0
g=0
e=0
for c in Mot:
    d=d+1
    if d % 3 == 0 :
        if c in Dic3:
            Dic3[c]=Dic3[c]+1
        else:
            Dic3[c]=1
    else:
         f=f+1
         if f % 2 == 0 : 
             if c in Dic2:
                 Dic2[c]=Dic2[c]+1
             else:
                 Dic2[c]=1
         else:
            if c in Dic1:
                 Dic1[c]=Dic1[c]+1
            else:
                 Dic1[c]=1
print(Dic1)
      
for x in Dic1:   
    print (x,':',Dic1[x])
    
print("-----------------------------------")

for y in Dic2:   
    print (y,':',Dic2[y])
    
print("-----------------------------------")

for z in Dic3:   
    print (z,':',Dic3[z])

L=ord('h')
print(L)
C=ord('e')
Borne= L-C
print(Borne)

L=ord('|')
print(L)
C=ord('s')
Borne2= L-C
print(Borne2)

L=ord('g')
print(L)
C=ord('e')
Borne3= L-C
print(Borne3)
Nouv=""
for i in Mot:
    e=e+1
    if e%3==0:
        Chiffre=ord(i)
        Decal=chr(Chiffre-Borne)
        Nouv=Nouv+Decal
    else:
        g=g+1
        if g%2 ==0:
            Chiffre=ord(i)
            Decal=chr(Chiffre-Borne2)
            Nouv=Nouv+Decal
        else:
            Chiffre=ord(i)
            Decal=chr(Chiffre-Borne3)
            Nouv=Nouv+Decal
print(Nouv[:20])
