from Crypto.Cipher import DES
import binascii, sys

key1= "Iam noob"
key2= "Uarenoob"
cipher="bc57426f605dadc74b169b2a1cf2ebd1d38f85fdcca12b16"

cipher_encrypt = DES.new(key2, DES.MODE_ECB)

cipher_decrypt= DES.new(key1, DES.MODE_ECB)

ct1 = cipher_decrypt.decrypt(binascii.unhexlify(cipher))

ct2 = cipher_encrypt.encrypt(ct1)

flag = cipher_decrypt.decrypt(ct2)
print(flag)