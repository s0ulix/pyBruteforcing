from Crypto.Cipher import AES
import binascii, sys

KEY = "3N7g309d6Y7enT1p"
plain2 = "a joke, mind it."

cipher2= "3a4911ae86c1f5138c2d8e17e7721658"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,plain2)
    return aes.decrypt(cipher)

# Output result
print "Decrypted data: " + binascii.hexlify(decrypt(binascii.unhexlify(cipher2), KEY))