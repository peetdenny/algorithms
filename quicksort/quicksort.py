def swap_dems(A, a, b):
	temp = A[a]
	A[a] = A[b]
	A[b] = temp


def choosePivot(A, p, right):
	return p


def sort(A, left, right):
	if len(A) < 2:
		return A
	if left >= right:
		return A
	pivot = choosePivot(A, left, right)
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
