from Crypto.Util.number import *
a="7A392A1577F7921D840A5DD8BC5C2C184DE17387E68D6168,b15bfdaa5c0e3a1ae9d2b435cdee81eba9e037d99bae6fb7f79bb00a6e1903fb"
pt=bytes_to_long(a)
print(pt)
p=getPrime(1024)
q=getPrime(16)
n=p*q
e=65537
ct=pow(pt,e,n)

opt="N : "+str(n)+"\ne : "+str(e)+"\nct : "+str(ct)+"\n"

ob=open("o.txt","w")
ob.write(opt)
ob.close()
