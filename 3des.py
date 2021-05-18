from Crypto.Cipher import DES3
import binascii, sys

key = "7A392A1577F7921D840A5DD8BC5C2C184DE17387E68D6168"

ct = "b15bfdaa5c0e3a1ae9d2b435cdee81eba9e037d99bae6fb7f79bb00a6e1903fb"

cipher_decrypt = DES3.new(binascii.unhexlify(key), DES3.MODE_ECB)

flag = cipher_decrypt.decrypt(binascii.unhexlify(ct))
print(flag)
