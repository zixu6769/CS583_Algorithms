
def quickSort(A, p, r):
	if (p < r):
		q = partition(A, p ,r)
		quickSort(A, p, q - 1)
		quickSort(A, q + 1, r)

def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if (A[j] <= x):
			i += 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[i + 1]
	A[i + 1] = A[r]
	A[r] = temp
	return i + 1


if __name__ == '__main__':
	A = [2,8,7,1,3,5,6,4]
	quickSort(A, 0, len(A)-1)
	print(A)
