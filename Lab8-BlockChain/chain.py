import hashlib
import time

def calculate_seed(seed):
	return seed.swapcase()

def calculate_hash(seed):
	hash = hashlib.md5()
	hash.update(seed.encode('utf-8'))
	return hash

seed = calculate_seed("ECSC")
hash = calculate_hash(seed)
iterations = 1
expected = "c89aa2ffb9edcc6604005196b5f0e0e4"
word = hash.hexdigest()
tmp = ""

while word != expected:
	iterations = iterations + 1
	tmp = word
	hash = calculate_hash(word)
	word = hash.hexdigest()
print ("Previous Hash " + tmp)
print ("WORD  " + word)
print ("Iterations  " + str(iterations))