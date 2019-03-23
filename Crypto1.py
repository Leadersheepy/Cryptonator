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
#Mot=""
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


#fichier = open("message2.txt", encoding="utf-8")
#Mot=fichier.read()
Mot="""9}¢M|7|M 7ā¡|M7x[7}x 
 7zM÷M7 E7!y|Mz}|M{7pĀ x7¡7¢
77|Mz7T7|7¢
7 ¡¡¡
M
DyĖ¢|MQM7¢|Mzz¡ÿ|M{7>yY7
Mx¡7¢
Mx¢|Mzz¡ÿ|[7{¡M¢>zCMTxx|¡7|M7¡|MM
Ėz x
¡7 7¥7|¡|M 7Ā 
7>
 |y|M{M¦| 7 y| 7xM7| ~RM{
7 7x¡|¢Y7¡7yMz
¡
¡7¡¢MM¦| 7|MTl|Y7MMz}| CMM¡M
¢| CM¢| CMM| zY7 x¢ 7|M~|Y7z¡7@[77\7¡|MĀx¡Y7
M|}z¡7¢
7|¢7|MT|7| 7 yM{7>y[7|
M|M{7£M¢MzM¢|¢| 7M¢|M7}7|MZĖM| Mĕ7č7>ď~7| 7x¡|¢ 7U|¡7ā|M÷M7x
M7¢xMTx¡¢|7M7|M} xM{ĕM7voĕ7 ĕz|VEMd 7MMxM{¥7M{TxĀM{7>¡|MQ7¢ 7
M¡xM¢M7
|M{T7}7ZxxĀ¡CM7¢xMzM|M¡x¡
M{M¡M 7|¥|M¢>¢
M7Āxx|[7M7¡ |M7|¢7¡|Y7|M
7|M ¡Ā 7|MzĀ 7
¡|Mz
 Āx
¡EM\7}|¡CM7¢
Mxx|¡7č77 yY7MMxM
M{Ėz~M [7rM7¦778M?x|7@M¡x¡
 7|MTxx|¡7Uz77¡7
M 7
77@[7|
MxM
¡77>¡7
MĖĖ7 |§7£
Ėy|[!
M¡7 7¢
7 ¡¡¡
M{}Ā|7 |7xM7Mzz¡ÿ|M{
 7|M x|[7|
M|xMxM{7}7ZxxĀ¡E7!y|M x|M¢|M 7£||§7|M{Ėz}|7¡7¢
77 |M{7}7ZxxĀ¡EMf77 M{Tx|7|¢M¢y ¢MM{Ėz~M{7xĕ7Ā{¢|M|7z¡
M{7 ¡
 7xM|¡7x[7n¡|
Mx
 M{M¢y ¢MM{Ėz~7|M
ÿ|MĖ7¡7|M¢>
Mx|M7}7|Mm~
ĕEMc7Ė7¡7¡¡Ė|M{7xM¢¡|M{M{Ėz~M¢>
M{¡7}|¢|EMc7| ~7 
¡7¡7}Ė7č7>|M{T7|M{7|ÿ|M 7|M
7£¢M{MM7~¢|¢M{7xMzĀM8M×M 7> x¦|7|M7¡£|7x7£¢MėEMl7|¡¡7
|Y7MMĖĖM{7¡7~M{
 7|M¡|Mz}Ā[7~7|¢Z7x
x
¡7 M¢MMĀx 7
¡7|¢MĖĖMV7!ZD7aĂ"""
Taille=len(Mot)
Dic={}

Chiffre=0
Nombre=0
Borne=0


for c in Mot:
    if c in Dic:
        Dic[c]=Dic[c]+1
    else:
        Dic[c]=1
print(Dic)

Lettre=input('1- Tu veux te baser sur quel lettre pour ?:')
L=ord(Lettre)
print(L)
Chi=input('1-Tu veux la transformer en quoi ?:')
C=ord(Chi)

print(C)
Borne= L-C
print(Borne)
Nouv=""
for i in range(Taille):
    Chiffre=ord(Mot[i])
    Nombre=chr(Chiffre-Borne)
    Nouv=Nouv+Nombre
print(Nouv)
















