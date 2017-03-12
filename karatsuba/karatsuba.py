def carrot(x, y):
	#   Test for base case
	#   Get length of X and Y. If > 2, not base case
	print('x',x,'y',y)
	len_x = len(str(x))

	n = len_x  # TODO generalise this to unequal n

	base_case = True
	if len_x > 2:
		base_case = False

	# Find index of middle of number
	divisor = (10 ** (n / 2))

	a = int(x / divisor)
	b = int(x % divisor)
	c = int(y / divisor)
	d = int(y % divisor)

	t1 = a * c if base_case else carrot(a, c)
	t2 = b * d if base_case else carrot(b, d)
	t3 = (a + b) * (c + d) if base_case else carrot((a + b), (c + d))
	t4 = t3 - t2 - t1
	t5 = (t1 * (10 ** n)) + t2 + (t4 * 10 ** (n / 2))
	return t5
