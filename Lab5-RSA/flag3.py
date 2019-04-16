from Crypto.PublicKey import RSA
###Open the file containing the key
f = open("mykey2", "r")
###Read the privateKey
privateKey = f.read()
###Create a new RSA object
key = RSA.importKey(privateKey)
###Extract the generated values
print (key.n)
print (key.e)
print (key.d)


