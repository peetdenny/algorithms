import sys

def sigma(max):
	if max <1: 
		return 0
	else:
		return max + sigma(max-1)


if __name__ == '__main__':
	print sigma(int(sys.argv[1]))
