import argparse


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


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Convertir la lettre en majuscule pour simplifier les calculs
            char = char.upper()

            # Décaler la lettre en utilisant la clé pour le déchiffrement
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            # Ajouter la lettre déchiffrée au texte déchiffré
            plaintext += decrypted_char

            # Passer à la lettre suivante de la clé
            key_index += 1
        else:
            # Ajouter les caractères non alphabétiques tels quels
            plaintext += char

    return plaintext


def encrypt_text(plaintext, key):
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Texte chiffré :", encrypted_text)


def decrypt_text(ciphertext, key):
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("Texte déchiffré :", decrypted_text)


def crack_vigenere(ciphertext):
    # Sélectionner toutes les clés possibles (combinant des lettres majuscules)
    keys = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    for key in keys:
        decrypted_text = vigenere_decrypt(ciphertext, key)
        print(f"Clé {key}: {decrypted_text}")


def main():
    """Fonction main"""
    parser = argparse.ArgumentParser(description='Programme de chiffrement et de déchiffrement de texte utilisant le chiffre de Vigenère')
    subparsers = parser.add_subparsers(dest='command', help='Commande à exécuter')
    
    # Commande d'encryption
    encrypt_parser = subparsers.add_parser('encrypt', help='Chiffrer un texte')
    encrypt_parser.add_argument('plaintext', help='Texte à chiffrer')
    encrypt_parser.add_argument('key', help='Clé de chiffrement')

    # Commande de déchiffrement
    decrypt_parser = subparsers.add_parser('decrypt', help='Déchiffrer un texte')
    decrypt_parser.add_argument('ciphertext', help='Texte à déchiffrer')
    decrypt_parser.add_argument('key', help='Clé de chiffrement')
    
    # Commande de cassage du chiffrement
    crack_parser = subparsers.add_parser('crack', help='Casser le chiffrement')
    crack_parser.add_argument('ciphertext', help='Texte chiffré')

    args = parser.parse_args()

    if args.command == 'encrypt':
        encrypt_text(args.plaintext, args.key)
    elif args.command == 'decrypt':
        decrypt_text(args.ciphertext, args.key)
    elif args.command == 'crack':
        crack_vigenere(args.ciphertext)


if __name__ == '__main__':
    main()


#exemple d'utilisation
"""python nom_du_programme.py encrypt "texte à chiffrer" "clé de chiffrement"
python nom_du_programme.py decrypt "texte chiffré" "clé de chiffrement"
python nom_du_programme.py crack "texte chiffré""""
