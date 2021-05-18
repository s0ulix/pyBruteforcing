from Crypto.Cipher import AES
import binascii, sys

KEY = "3N7g309d6Y7enT1p"
plain2 = " But complete se"

cipher2= "e764f66e54397534f7d049506acabb2c"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,plain2)
    return aes.decrypt(cipher)

# Output result
print "Decrypted data: " + binascii.hexlify(decrypt(binascii.unhexlify(cipher2), KEY))
