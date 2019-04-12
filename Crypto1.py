# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:37:00 2019
http://naelshiab.com/python-et-la-cryptographie-et-un-peu-de-piratage-aussi/?fbclid=IwAR1n9Noep7Aojy6Jys7BjNbuE0JDyUrR3k86cBURq35IFTLQkfqrPMsbgNg
@author: Villebon
"""
#-------------------------------------------------
#-------------------------------------------------
#
#"""fichier = open("message1.txt", encoding="utf-8")
#Mot=fichier.read()"""
#Mot= "JuL dreioVet srom.s dlo "
#Taille=len(Mot)
#M=int(input('Taille:'))
#b = True
#for cle in range(2,M):
#    Nouv=""
#    for i in range(cle):
#        for j in range(i,Taille,cle):
#            Nouv=Nouv+Mot[j]
##        print(cle)
##        print(Nouv[:15])
#    if Nouv[:2]=="Je":
#        b = False
#        print(Nouv[:15])
#        print(cle)
#
#if b:
#    print("il n'y a pas :(")
###    
#7
#-------------------------------------------------
#-------------------------------------------------
#
#fichier = open("message1.txt", encoding="utf-8")
#Mot=fichier.read()
#"""Mot= "JuL dreioVet srom.s dlo""" 
#
#Taille=len(Mot)
#M=int(input('Taille:'))
#b = True
#i=0
#Nouv=""
#while i<M and Nouv[:14]!= "Fonctionnement":
#    for cle in range(2,M):
#        for i in range(cle):
#            for j in range(i,Taille,cle):
#                Nouv=Nouv+Mot[j]
#                print(Nouv[:15])
#                print(cle)
#    

#fichier = open("message1.txt", encoding="utf-8")
#Mot=fichier.read()
##Mot= "JuL dreioVet srom.s dlo "
#Taille=len(Mot)
#M=int(input('Taille:'))
#b = True
#for cle in range(2,M):
#    Nouv=""
#    for i in range(cle):
#        for j in range(i,Taille,cle):
#            Nouv=Nouv+Mot[j]
##        print(cle)
##        print(Nouv[:15])
#    if Nouv[:2]=="Je":
#        b = False
#        print(Nouv[:15])
#        print(cle)
#
#if b:
#    print("il n'y a pas :(")  

#----------------------------------MESSAGE 2 et 3----------------------------------#  
#fichier = open("message2.txt", encoding="utf-8")
#Mot=fichier.read()
#Mot=""
#Taille=len(Mot)
#Borne=int(input('Chiffre de César:'))
#Chiffre=0
#Nombre=0
#for decalage in range (Borne):
#    Nouv=""
#    for i in range(Taille):
#        Chiffre=ord(Mot[i])
#        Nombre=chr(Chiffre-decalage)
#        Nouv=Nouv+Nombre
#    if Nouv[-4:]=="Joël":
#        b = False
#        print(decalage)
#        print(Nouv)  
##-----------------------------------------------------------------------------#
##----------------------------------MESSAGE 4----------------------------------#  
##fichier = open("message2.txt", encoding="utf-8")
##Mot=fichier.read()
#Mot="ABCD"
#Taille=len(Mot)
#Borne=int(input('Chiffre de César:'))
#Chiffre=0
#Nombre=0
#for decalage in range (Borne):
#    Nouv=""
#    for i in range(Taille):
#        Chiffre=ord(Mot[i])
#        Nombre=chr(Chiffre-decalage)
#        Nouv=Nouv+Nombre
#    if Nouv[-4:]=="Joël":
#        b = False
#        print(decalage)
#        print(Nouv)  
#-----------------------------------------------------------------------------#
#----------------------------------MESSAGE 2 et 3----------------------------------#  
#fichier = open("message2.txt", encoding="utf-8")
#Mot=fichier.read()
##Mot=""
#Taille=len(Mot)
#Dic={}
#Chiffre=0
#Nombre=0
#Borne=0
#for c in Mot:
#    if c in Dic:
#        Dic[c]=Dic[c]+1
#    else:
#        Dic[c]=1
#print(Dic)
##Borne=int(input('Chiffre de César:'))
#Lettre=input('Tu veux te baser sur quel lettre ?:')
#L=ord(Lettre)
#print(L)
#
#Chi=input('Tu veux la transformer en quoi ?:')
#C=ord(Chi)
#
#print(C)
#Borne= L-C
#print(Borne)
#Nouv=""
#for i in range(Taille):
#    Chiffre=ord(Mot[i])
#    Nombre=chr(Chiffre-Borne)
#    #Nombre=chr(((Chiffre-ord('a')+Borne)%26)+ord('a'))
#    Nouv=Nouv+Nombre
#print(Nouv)

###MESSAGE 4 ###
#23
#def carac_plus_frequent(Dic):
#    m = -1
#    for car in Dic:
#        if m < Dic[car]:
#            m = Dic[car]
#            c_plus_frequent = car
#    return c_plus_frequent
#    
#Mot="""¡7|¢MĖĖMV7!ZD7aĂ"""
fichier = open("message4.txt", encoding="utf-8")
Mot=fichier.read()
Taille=len(Mot)
Dic={}
Dic2={}
Chiffre=0
Nombre=0
Borne=0
d=0
e=0
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
            
for x in Dic:   
    print (x,':',Dic[x])
    
print("-----------------------------------")

for y in Dic2:   
    print (y,':',Dic2[y])        

#print(Dic2['c'])
#c1 = carac_plus_frequent(Dic)
#c2 = carac_plus_frequent(Dic2)
#print(c1)
#print(c2) | 

Lettre=input('1-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
Chi=input('1-Tu veux la transformer en quoi ?:')
C=ord(Chi)
Borne= L-C
print(Borne)

Lettre=input('2-Tu veux te baser sur quel lettre ?:')
L=ord(Lettre)
print(L)
Chi=input('2-Tu veux la transformer en quoi ?:')
C=ord(Chi)
Borne2= L-C
print(Borne2)
TabBorne=[Borne,Borne2]
Nouv=""

for i in range (Taille):
    e=e+1
    Chiffre=ord(Mot[i])
    Caract=chr(Chiffre+TabBorne[i%2])
    Nouv=Nouv+Caract

print(Nouv[:20])
 



