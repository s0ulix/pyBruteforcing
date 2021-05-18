import random

key = "l"

c="0f150e091e040d0f07173f1c5f021833013533205d0a5f331f181928355d222b33345c3e11"
ct=(c).decode('hex')
ciphertext = ""
for i in range(len(ct)):
	ciphertext += chr(ord(key) ^ ord(ct[i]));
print(ciphertext)