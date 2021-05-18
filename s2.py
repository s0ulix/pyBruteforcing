from Crypto.Cipher import AES
import binascii, sys

KEY = "3N7g309d6Y7enT1p"
plain2 = "curity is a myth"

cipher2= "dabc02a058f8c3936a5fd6ddd3c50491"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,plain2)
    return aes.decrypt(cipher)

# Output result
print "Decrypted data: " + binascii.hexlify(decrypt(binascii.unhexlify(cipher2), KEY))
