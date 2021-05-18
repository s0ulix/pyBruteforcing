import hashlib
import sys
check="af0fb1ba9622c3a513cfd3f40537d3e37b13c5c0a425260b17306aa2d5d6c68c918b263ef0bb04dc95c361887ad650217daaf7180e94321e304f3d3d12e561b9"
crib='pastebin.com/GtEz'
a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
for b in a:
	for c in a:
		for d in a:
			for e in a:
				hash_string = crib+b+c+d+e
				sha_signature = hashlib.sha512(hash_string.encode()).hexdigest()
				if(sha_signature==check):
					print(b+c+d+e)
					sys.exit()