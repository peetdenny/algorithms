import random
comps = 0


def swap_dems(A, a, b):
	temp = A[a]
	A[a] = A[b]
	A[b] = temp


def choose_pivot(A, left, right):
	pivot = random.randrange(left, right)
	swap_dems(A, left, pivot)
	return left


def sort(A, left, right):
	if len(A) < 2:
		return A
	if left >= right:
		return A
	global comps
	comps += (right - left)
	pivot = choose_pivot(A, left, right)

	i = left + 1

	for j in range(i, right +1):
		if A[j] < A[pivot]:
			swap_dems(A, i, j)
			i += 1

	swap_dems(A, pivot, i-1)

	if len(A) < 3:
		return A

	sort(A, left, i-2)
	sort(A, i, right)

	return A
