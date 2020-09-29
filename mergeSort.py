import math

def merge(A, p, q, r):
	left_n = q - p + 1
	right_n = r - q

	left_A = [None] * (left_n + 1)
	right_A = [None] * (right_n + 1)

	for i in range(0, left_n):
		left_A[i] = A[p + i]
	for j in range(0, right_n):
		right_A[j] = A[q + j + 1]

	left_A[left_n] = math.inf
	right_A[right_n] = math.inf

	i = 0
	j = 0

	for k in range(p, r + 1):
		if (left_A[i] <= right_A[j]):
			A[k] = left_A[i]
			i += 1
		else:
			A[k] = right_A[j]
			j += 1

def mergeSort(A, p, r):
	if (p < r):
		q = math.floor((p + r) / 2)
		mergeSort(A, p, q)
		mergeSort(A, q + 1, r)
		merge(A, p, q, r)
		return A

if __name__ == '__main__':
	array = [3,5,2,1,6,7,100,32]
	print(mergeSort(array, 0, len(array)-1))