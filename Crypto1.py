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

#----------------------------------MESSAGE 2----------------------------------#  
fichier = open("message2.txt", encoding="utf-8")
Mot=fichier.read()
#Mot=""
Taille=len(Mot)
Borne=int(input('Chiffre de César:'))
Chiffre=0
Nombre=0
for decalage in range (Borne):
    Nouv=""
    for i in range(Taille):
        Chiffre=ord(Mot[i])
        Nombre=chr(Chiffre-decalage)
        Nouv=Nouv+Nombre
    if Nouv[-4:]=="Joël":
        b = False
        print(decalage)
        print(Nouv)