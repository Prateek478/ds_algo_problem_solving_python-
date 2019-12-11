'''Caesar cipher encryptor and decryptor
Examples :
  Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
  Shift: 23
  Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

  Text : ATTACKATONCE
  Shift: 4
  Cipher: EXXEGOEXSRGI

Input:
  -A String of lower case letters, called Text.
  -An Integer between 0-25 denoting the required shift.
'''

# Caesar Cipher
import random
MAX_KEY_SIZE = 26

def get_mode():
    while True:
        print('Do you wish to encrypt or decrypt a message? Enter either "encrypt" or "e" or "decrypt" or "d"')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d"')


def get_message():
    print('Enter your message:')
    return input()


def get_key():
    print ("Enter the key between 1-%s" % MAX_KEY_SIZE)
    key = int(input())
    return key
    
def get_translated_message(mode, message, key):
    translated = ''
    if mode[0] == 'e':
        key = -key
    for symbol in message:
        if symbol.isalpha():
            alpha_key = key%26
            num = ord(symbol)
            print
            num = num + alpha_key
            if symbol.isupper():
                if num > ord('Z'):
                    num = num -26
                elif num < ord('A'):
                    num = num+26
            elif symbol.islower():
                if num > ord('z'):
                    num = num -26
                elif num < ord('a'):
                    num = num+26
            print(num)
            translated += chr(num)
        elif symbol.isdigit():
            alpha_key = key % 10
            num = ord(symbol)
            num = num + alpha_key
            if not chr(num).isdigit():
                num = num - 10
            print(num)
            translated += chr(num)
        else:
            translated += symbol
    return translated
    
if __name__ == "__main__":
    mode = get_mode()
    message = get_message()
    key = get_key()
    print ("Key is %s" % key)

    print('Your translated text is:')
    print(get_translated_message(mode, message, key))
