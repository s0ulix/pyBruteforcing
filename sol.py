from Crypto.Cipher import DES3
import binascii, sys

key = "Iam noobUarenoob"

ct = "bc57426f605dadc74b169b2a1cf2ebd1d38f85fdcca12b16"

cipher_decrypt = DES3.new(key, DES3.MODE_ECB)

flag = cipher_decrypt.decrypt(binascii.unhexlify(ct))
print(flag)
