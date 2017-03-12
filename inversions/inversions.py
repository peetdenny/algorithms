# create a recursive algorithm that counts recurses down the base case of an array of two
# numbers. Count the number of inversions-go in each side, and then once you've done that,
# count the number of split inversions-go.
# inversions-go can either be in array L, array R or split between the two.

# returns sorted array, plus number of inversions-go counted. An inversion is when


def handle_base_case(a):
	if len(a) == 1:
		return a, 0
	if a[0] > a[1]:
		return [a[1], a[0]], 1
	return a, 0


def count_inversions(a):
	# is base case?
	if len(a) <= 2:
		return handle_base_case(a)
	n = len(a)
	pivot = int(n / 2)
	L, left_count = count_inversions(a[0:pivot])
	R, right_count = count_inversions(a[pivot:])
	O, split_count = count_n_merge_split_inversions(L, R)
	inversions = O, left_count + right_count + split_count
	return inversions


def count_n_merge_split_inversions(l, r):
	# this is the same as the merge from mergesort, but performs a count as it merges
	lidx = ridx = 0
	output_array = [len(l) + len(r)]
	split_count = 0
	while lidx < len(l):
		if l[lidx] < r[ridx]:
			output_array.append(l[lidx])
			lidx += 1
			if lidx >= len(l):
				output_array.extend(r[ridx:])
				return output_array, split_count

		else:
			output_array.append(r[ridx])
			ridx += 1
			split_count += len(l) - lidx
			print('split count', split_count)
	return output_array, split_count
