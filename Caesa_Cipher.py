# Caesar Cipher
import time
SYMBOLs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLs)

def getMode():
    while True:
        print('Do u wish to encrypt or decrypt or brute-force a message?')
        mode = input().lower()
        if mode in 'encrypt decrypt brute-force e d b'.split():
            return mode
        else:
            print('Please enter either "encrypt"("e") or "decrypt"("d") or "brute-force"("b")!')

def getMessage():
    print('Enter ur message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-{})'.format(MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key

def getTranslateMessage(mode, message, key):

    if mode[0] == 'd': key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLs.find(symbol)
        if symbolIndex == -1:
            translated += symbol

        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLs):
                symbolIndex -= len(SYMBOLs)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLs)

            translated += SYMBOLs[symbolIndex]
    
    return translated

if __name__=='__main__':
    mode = getMode()
    message = getMessage()
    if mode[0] != 'b': key = getKey()
    if mode[0] != 'b': 
        print('Your translated text is:')
        print(getTranslateMessage(mode, message, key))
    else:
        print('Brute-forcing the message:')
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, getTranslateMessage('decrypt', message, key))
            time.sleep(0.5)