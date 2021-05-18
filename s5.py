from Crypto.Cipher import AES
import binascii, sys

KEY = "3N7g309d6Y7enT1p"
IV="Security is not "
    
cipher1="54453ced1207bb9f67894d2c8ae336d4"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,IV)
    return aes.decrypt(cipher)

print "decrypted data: " + decrypt(binascii.unhexlify(cipher1), KEY)