import random
import string

crypt = " " + string.ascii_letters + string.punctuation + string.digits
crypt = list(crypt)
key = crypt.copy()

random.shuffle(key)

#Encrypting

message = input('Digit the phrase you want to encrypt: ')
cipher_text = ''

for letter in message:
    index = crypt.index(letter)
    cipher_text += key[index]

#print the process

print(f'\nOriginal message: {message}')
print(f'Encrypted message: {cipher_text}')

password = input('\nDigit your password to decrypt: ')

#Decrypting

message_decrypted = input('\nDigit the phrase you want to decrypt: ')
password_verification = input('The password that you choose to decrypt: ')
message_now = ''

#decrypting process

def decrypting(cipher_text, message_now, crypt):
    for letter in cipher_text:
        index = key.index(letter)
        message_now += crypt[index]

#password verification, if it's wrong, it will keep asking for the correct password

if password_verification == password:
    decrypting(cipher_text, message_now, crypt)

else:
    password_verification = input('Wrong password, try again the password that you choose to decrypt: ')
    while password_verification != password:
        if password_verification == password:
            decrypting(cipher_text, message_now, crypt)
        password_verification = input('Wrong password, try again the password that you choose to decrypt: ')

print(f'\nDecrypted message: {message}')

print('\nThanks for the support, this was just a simple cryptography program that i made to pratice my programming logic!')
input('Press enter to close this window!')