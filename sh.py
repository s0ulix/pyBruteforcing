import hashlib
hash_string="pastebin.com/GtEzr2xY"
sha_signature = hashlib.sha512(hash_string.encode()).hexdigest()
print(sha_signature)