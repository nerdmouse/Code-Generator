"""
This program will take a string of text inputed by the user, and it will replace it with
another letter. It will ignore spaces, and only replace capital letters with another
capital letter, lowercase letters with lowercase, numbers with other numbers, and
punctuation will not be replaced
"""
import random

input_text = input("Please enter text: \n")
rencrypted_text = ""
encrypted_text = ''

print("This is just randomly doing it")

for x in input_text:
    if (x >= 'a' and x <= 'z'):
        x = chr((random.randint(97, 122)))
        rencrypted_text = rencrypted_text + x
    elif (x >= 'A' and x <= 'Z'):
        x = chr(random.randint(65, 90))
        rencrypted_text = rencrypted_text + x
    elif (x >= '0' and x <= '9'):
        x = chr(random.randint(48, 57))
        rencrypted_text = rencrypted_text + x
    else:
        rencrypted_text = rencrypted_text + x

print(rencrypted_text + "\n\n")

print("This is using a Caesar Cipher\n")
shift_amount = int(input("Choose a shift pattern: "))
tempc = 0

for x in input_text:
    if (x >= 'a' and x <= 'z'):
        tempc = (ord(x) + shift_amount)
        if (tempc > 122):
            tempc = tempc - 26
        encrypted_text = encrypted_text + chr(tempc)
    elif (x >= 'A' and x <= 'Z'):
        tempc = (ord(x) + shift_amount)
        if (tempc > 90):
            tempc = tempc - 26
        encrypted_text = encrypted_text + chr(tempc)
    elif (x >= '0' and x <= '9'):
        tempc = (ord(x) + shift_amount)
        if (tempc > 57):
            tempc = tempc - 10
        encrypted_text = encrypted_text + chr(tempc)
    else:
        encrypted_text = encrypted_text + x

print(encrypted_text)
