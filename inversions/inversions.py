a1 = [1,2,3,5,4,6,9,8,7]


# create a recursive algorithm that counts rescurses down the base case of an array of two
# numbers. Count the number of inversions in each side, and then once you've done that,
# count the number of split inversions.
# inversions can either be in array L, array R or split between the two.

def count_inversions(a1):
	if len(a1) <=1:
		return 0
	if len(a1) <=2:
		if a1[0] > a1[1]:
			return 1
		return 0

	# not base case, so recurse
	n = len(a1)
	pivot = int((n/2))
	L = a1[0:pivot]
	R = a1[pivot:]
	l_count = count_inversions(L)
	r_count = count_inversions(R)
	# get split count
	return l_count + r_count

print('found', count_inversions(a1), 'inversions')
