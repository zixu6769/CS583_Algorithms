from insertionSort import *
import math

def bucketSort(A):
	n = len(A)
	B = [[] for i in range(n)]
	result = []
	for i in range(0, n):
		B[math.floor(n*A[i])].append(A[i])
	for i in range(0, n):
		insertionSort(B[i])
	for i in range(0, n):
		for element in B[i]:
			result.append(element)
	return result

if __name__ == '__main__':
	A = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
	print(bucketSort(A))

	
