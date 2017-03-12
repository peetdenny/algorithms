import sys


def sigma(mx):
	if mx < 1:
		return 0
	else:
		return mx + sigma(mx - 1)


if __name__ == '__main__':
	print(sigma(int(sys.argv[1])))
