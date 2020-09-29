def insertionSort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0 and A[i] > key):
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key
	return A

if __name__ == '__main__':
	array = [3,5,2,1,6,7,100,32]
	print(insertionSort(array))