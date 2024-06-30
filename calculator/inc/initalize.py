import string
import random

def init_key():
	key = ""
	characters = string.ascii_letters + string.digits
	string_key = "".join(random.choice(characters) for _ in range(16))
	
	for i in range(16):
		key += string_key[i]
		
		if (i % 4 == 3) and (i != 15):
			key += " - "
			
	return key
			
