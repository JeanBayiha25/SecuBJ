#!/usr/bin/python
#-*-coding:utf8-*-
import argparse

""" Décale de n place(s) dans la table ASCII """
def letterShift(letter, n):
    return chr((ord(letter) + n) % 255)

""" Crypte un texte """
def encryptText(text, n):
    encryptText = ""

    for i in range(0, len(text)):
        character = text[i]

        if character != " ":
            encryptText = encryptText + letterShift(character, n)
        else:
            encryptText = encryptText + " "

    return encryptText

""" Décrypte un texte """
def decryptText(text, n):
    decryptText = ""

    for i in range(0, len(text)):
        character = text[i]

        if character != " ":
            decryptText = decryptText + letterShift(character, int("-" + str(n)))
        else:
            decryptText = decryptText + " "

    return decryptText

""" Crypte un texte avec une clé saisie par l'utilisateur """
def encryptTextKey(text, key):
    encryptText = ""

    for i in range(0, len(text)):
        character = text[i]

        if character != " ":
            encryptText = encryptText + letterShift(character, int(key[i % len(key)]))
        else:
            encryptText = encryptText + " "

    return encryptText

""" Décrypte le texte avec la clé saisie par l'utilisateur """
def decryptTextKey(text, key):
    decryptText = ''

    for i in range(0, len(text)):
        character = text[i]

        if character != " ":
            decryptText = decryptText + letterShift(character, int("-" + str(key[i % len(key)])))
        else:
            decryptText = decryptText + " "

    return decryptText

"""Crypte le contenu d'un fichier texte"""
def encryptFile(file, key):
    file = open(file, 'r')
    text = file.read()
    file.close()
    encryptFile = encryptTextKey(text, key)
    file = open('texte_crypte', 'w')
    file.write(encryptFile)
    file.close()

"""Décrypte le contenu d'un fichier"""
def decryptFile(file, key):
    file = open(file, 'r')
    encryptText = file.read()
    file.close()
    decryptText = decryptTextKey(encryptText, key)
    file = open('texte_decrypte', 'w')
    file.write(decryptText)
    file.close()

def main():
    """Fonction main"""
    parser = argparse.ArgumentParser(description='Programme de chiffrement et de déchiffrement de texte')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode d\'opération : encrypt (chiffrement) ou decrypt (déchiffrement)')
    parser.add_argument('-t', '--text', help='Texte à chiffrer ou déchiffrer')
    parser.add_argument('-k', '--key', help='Clé de chiffrement')
    parser.add_argument('-f', '--file', help='Fichier à chiffrer ou déchiffrer')

    args = parser.parse_args()

    if args.mode == 'encrypt':
        if args.text and args.key:
            encryptedText = encryptTextKey(args.text, args.key)
            print("Texte crypté : ", encryptedText)
        elif args.file and args.key:
            encryptFile(args.file, args.key)
            print("Fichier crypté avec succès.")
        else:
            print("Les arguments nécessaires sont manquants.")

    elif args.mode == 'decrypt':
        if args.text and args.key:
            decryptedText = decryptTextKey(args.text, args.key)
            print("Texte décrypté : ", decryptedText)
        elif args.file and args.key:
            decryptFile(args.file, args.key)
            print("Fichier décrypté avec succès.")
        else:
            print("Les arguments nécessaires sont manquants.")

if __name__ == '__main__':
    main()
