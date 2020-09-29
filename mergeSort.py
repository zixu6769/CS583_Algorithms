import math

def merge(a, p, q, r):
	left_n = q - p + 1
	right_n = r - q

	left_a = [None] * (left_n + 1)
	right_a = [None] * (right_n + 1)

	for i in range(0, left_n):
		left_a[i] = a[p + i]
	for j in range(0, right_n):
		right_a[j] = a[q + j + 1]

	left_a[left_n] = math.inf
	right_a[right_n] = math.inf

	i = 0
	j = 0

	for k in range(p, r + 1):
		if (left_a[i] <= right_a[j]):
			a[k] = left_a[i]
			i += 1
		else:
			a[k] = right_a[j]
			j += 1

def mergeSort(a, p, r):
	if (p < r):
		q = math.floor((p + r) / 2)
		mergeSort(a, p, q)
		mergeSort(a, q + 1, r)
		merge(a, p, q, r)
		return a