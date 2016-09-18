import sys
chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def get_hex_string(str,x):
	if(x < 16):
		return str + chars[int(x)]
	else:
		return get_hex_string(str, x/16) + chars[(int(x % 16))]

print get_hex_string('',float(sys.argv[1]))


