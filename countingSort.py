
def countingSort(A, k):
	C = [0] * (k + 1)
	result = [None] * len(A)

	# counting each element of A
	for j in range(0, len(A)): C[A[j]] += 1

	# calculate position of each element
	for i in range(1, k+1): C[i] += C[i-1]

	# write to result array
	for j in range(len(A)-1, -1, -1):
		result[C[A[j]]-1] = A[j]
		C[A[j]] -= 1

	return result

if __name__ == '__main__':
	A = [2,5,3,0,2,3,0,3]
	print(countingSort(A, 5))

	
