import js
from ciphercaesar import encrypt, decrypt

def genrt(*args, **kwargs):
    pass

while True:
    msg = input('msg (q for quit): ')
    if msg=='q':
        quit()
    else:
        pass
    k = int(input('key: '))
    print(encrypt(msg,k))