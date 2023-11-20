def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Convertir la lettre en majuscule pour simplifier les calculs
            char = char.upper()

            # Décaler la lettre en utilisant la clé
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            # Ajouter la lettre chiffrée au texte chiffré
            ciphertext += encrypted_char

            # Passer à la lettre suivante de la clé
            key_index += 1
        else:
            # Ajouter les caractères non alphabétiques tels quels
            ciphertext += char

    return ciphertext


def main():
    plaintext = input("Entrez le texte à chiffrer : ")
    key = input("Entrez la clé de chiffrement : ")

    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Texte chiffré :", encrypted_text)


main()

"""
Dans ce programme, la fonction vigenere_encrypt prend le texte en clair et la clé de chiffrement comme entrée et retourne le texte chiffré utilisant le chiffre de Vigenère.

La fonction itère sur chaque caractère du texte en clair. Si le caractère est une lettre alphabétique, il est converti en majuscule pour simplifier les calculs. Ensuite, la lettre est décalée en utilisant la clé correspondante. Le décalage est calculé en convertissant la lettre correspondante de la clé en un nombre de 0 à 25 (en utilisant la valeur ASCII) et en soustrayant la valeur de la lettre 'A'. Ensuite, le caractère chiffré est calculé en ajoutant le décalage au caractère en clair et en effectuant une opération modulo 26 pour assurer que le résultat reste dans la plage des lettres de l'alphabet. Enfin, la lettre chiffrée est ajoutée au texte chiffré.

Les caractères non alphabétiques (espaces, ponctuation, etc.) sont ajoutés tels quels au texte chiffré.

Dans la fonction main, vous pouvez entrer le texte à chiffrer et la clé de chiffrement. Le texte chiffré sera ensuite affiché à l'écran
"""
