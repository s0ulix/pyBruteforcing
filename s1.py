from Crypto.Cipher import AES
from operator import xor
import binascii, sys

KEY_first = "3N7g309d6Y7enT"
cipher1 = "e700000000000000000000000000bb2c" 
cipher2 = "dabc02a058f8c3936a5fd6ddd3c50491"
plain1 = " But complete se"
plain2 = "curity is a myth"

def decrypt(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, binascii.unhexlify(cipher1))
    return aes.decrypt(cipher)

# iterate through relavent ascii range
for i in range(32, 126):
    for j in range(32, 126):
        key = KEY_first + chr(i) + chr(j)
        dec_plain2 = decrypt(binascii.unhexlify(cipher2),  key)
        if  str(dec_plain2).startswith("c") and str(dec_plain2).endswith('th'):
            print "decrypted plain2: " + dec_plain2 + " with key: " + key