import binascii

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(message,key):
    M = toHex(message)
    K = toHex(key)
    code = M ^ K
    return code

def decrypt(code, key):
    K = toHex(key)
    C = code
    M = C ^ K
    return toString(M)

def main():
    setning = str(input("Skriv inn noe\n::: "))
    liste = []
    tegn = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    import random
    for i in range(len(setning)):
        liste.append(random.choice(tegn))
    key = ''.join(liste)
    kryptert = encrypt(setning, key)
    dekryptert = decrypt(kryptert, key)
    print(kryptert)
    print(dekryptert)

main()