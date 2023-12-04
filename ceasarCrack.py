# Import colorama for colorful text.
from colorama import Fore, init
import argparse

init()

# Define a function for Caesar cipher encryption.
def implement_caesar_cipher(text, key, decrypt=False):
    # Initialize an empty string to store the result.
    result = ""

    # Iterate through each character in the input text.
    for char in text:
        # Check if the character is alphabetical.
        if char.isalpha():
            # Determine the shift value using the provided key (or its negation for decryption).
            shift = key if not decrypt else -key

            # Check if the character is lowercase
            if char.islower():
                # Apply the Caesar cipher encryption/decryption formula for lowercase letters.
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Apply the Caesar cipher encryption/decryption formula for uppercase letters.
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # If the character is not alphabetical, keep it as is e.g. numbers, punctuation
            result += char

    # Return the result, which is the encrypted or decrypted text
    return result


# Define a function for cracking the Caesar cipher.
def crack_caesar_cipher(ciphertext):
    # Iterate through all possible keys (0 to 25) as there 26 alphabets.
    for key in range(26):
        # Call the caesar_cipher function with the current key to decrypt the text.
        decrypted_text = implement_caesar_cipher(ciphertext, key, decrypt=True)

        # Print the result, showing the decrypted text for each key
        print(f"{Fore.RED}Key {key}: {decrypted_text}")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Programme de décryptage du chiffre de César')
    parser.add_argument('text', help='Le texte chiffré à décrypter')

    args = parser.parse_args()

    if not args.text:
        parser.error('L\'option text est requise')

    crack_caesar_cipher(args.text)


if __name__ == '__main__':
    main()

#exemple d'utilisation
""" python ceasarCrack.py "texte_chiffré""""   
