"""
This program will take a string of text inputed by the user, and it will replace it with
another letter. It will ignore spaces, and only replace capital letters with another
capital letter, lowercase letters with lowercase, numbers with other numbers, and
punctuation will not be replaced
"""
import random

def caesar_cipher(_plain_text, _shift):
    plain_text = _plain_text
    shift = _shift
    encrypted_text = ''

    for x in plain_text:
        if (x >= 'a' and x <= 'z'):
            tempc = (ord(x) + shift)
            if (tempc > 122):
                tempc = tempc - 26
            encrypted_text = encrypted_text + chr(tempc)
        elif (x >= 'A' and x <= 'Z'):
            tempc = (ord(x) + shift)
            if (tempc > 90):
                tempc = tempc - 26
            encrypted_text = encrypted_text + chr(tempc)
        elif (x >= '0' and x <= '9'):
            tempc = (ord(x) + shift)
            if (tempc > 57):
                tempc = tempc - 10
            encrypted_text = encrypted_text + chr(tempc)
        else:
            encrypted_text = encrypted_text + x
    print(encrypted_text)

plain_text = input("Please enter text: \n")

print("This is using a Caesar Cipher\n")
shift_amount = int(input("Choose a shift pattern: "))

caesar_cipher(plain_text, shift_amount)
