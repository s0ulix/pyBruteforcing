from Crypto.Cipher import DES
import binascii, sys

key1= "Iam noob"
key2= "Uarenoob"
flag = "m4nu4l_3des_1s_th3_way:)"
cipher_encrypt = DES.new(key1, DES.MODE_ECB)

ct1 = cipher_encrypt.encrypt(flag)

cipher_decrypt= DES.new(key2, DES.MODE_ECB)

ct2 = cipher_decrypt.decrypt(ct1)

cipher= cipher_encrypt.encrypt(ct2)
print(binascii.hexlify(cipher))
