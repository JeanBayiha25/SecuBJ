#!/usr/bin/python
#-*-coding:utf8-*-

import sys
import os

""" 
    Décale de n place(s) dans la table ASCII
"""
def letterShift(letter, n):
    return chr((ord(letter) + n) % 255)
        
""" 
    Crypte un texte 
"""        
def encryptText(text, n):
    encryptText = ""
    
    for i in range(0, len(text)):
        character = text[i]
        
        if character != " ":
            encryptText = encryptText + letterShift(character, n)
        else:
            encryptText = encryptText + " "
    
    return encryptText


""" 
    Décrypte un texte 
"""
def decryptText(text, n):
    decryptText = ""
    
    for i in range(0, len(text)):
        character = text[i]

        if character != " ":
            decryptText = decryptText + letterShift(character, int("-" + str(n)))
        else:
            decryptText = decryptText + " "
            
    return decryptText


""" 
    Crypte un texte avec une clé saisie par l'utilisateur 
"""
def encryptTextKey(text, key):
    encryptText = "" 
    
    for i in range(0, len(text)):
        character = text[i]
        
        if character != " ":
            encryptText = encryptText + letterShift(character, int(key[i % len(key)]))
        else:
            encryptText = encryptText + " "
    
    return encryptText


""" 
    Décrypte le texte avec la clé saisie par l'utilisateur 
"""    
def decryptTextKey(text, key):
    decryptText = ''
    
    for i in range(0, len(text)):
        character = text[i]
        
        if character != " ":
            decryptText = decryptText + letterShift(character, int("-" + str(key[i % len(key)])))
        else:
            decryptText = decryptText + " "
    
    return decryptText
"""
    Crypte le contenu d'un fichier texte
"""
def encryptFile(file, key):
    file = open(file, 'r')
    text = file.read()
    file.close()
    encryptFile = encryptTextKey(text, key)
    file = open('texte_crypte', 'w')
    file.write(encryptFile)
    file.close()
   

"""
    Décrypte le contenu d'un fichier
"""
def decryptFile(file, key):
    file = open(file, 'r')
    encryptText = file.read()
    file.close()
    decryptText = decryptTextKey(encryptText, key)
    file = open('texte_decrypte', 'w')
    file.write(decryptText)
    file.close()


def main():
    """Fonction main """
    if __name__ == '__main__':
        print (" 1 -> Code de cesar")
        print (" 2 -> Code de cesar amelioré")
        choice = input("Choix : ")
        print()
        
        if choice == str("1"):
            encryptedText=""
            decryptedText=""
            print ("======= DONNEES =======")
            shift = input("Entrez le décalage souhaité : ")
            text = input("Entrez le texte à crypter : ")
            print ("======= CRYPTAGE =======")
            encryptedText = encryptText(text, int(shift))
            print ("Texte crypté : ", encryptedText)
            print ("======= DECRYPTAGE =======")
            decryptedText = decryptText(encryptedText, int(shift))
            print ("Texte décrypté : ", decryptedText)
        
        if choice == str("2"):
            encryptedText=""
            decryptedText=""
            print ("======= DONNEES =======")
            key = input("Entrez la clé de chiffrement : ")
            text = input("Entrez le texte à crypter : ")
            print ("======= CRYPTAGE =======")
            encryptedText = encryptTextKey(text, key)
            print ("Texte crypté : ", encryptedText)
            print ("======= DECRYPTAGE =======")
            decryptedText = decryptTextKey(encryptedText, key)
            print ("Texte décrypté : ", decryptedText)
        print()
        sys.exit(0)

main()
