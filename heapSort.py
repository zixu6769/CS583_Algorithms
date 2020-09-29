import math

def parent(i):
	return math.floor((i-1)/2)

def left(i):
	return 2*i + 1

def right(i):
	return 2*i + 2

def maxHeapify(A, i, size):
	l = left(i)
	r = right(i)
	if (l <= size-1 and A[l] > A[i]):
		largest = l
	else:
		largest = i
	if (r <= size-1 and A[r] > A[largest]):
		largest = r
	if (largest != i):
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		maxHeapify(A, largest, size)

def buildMaxHeap(A):
	size = len(A)
	for i in range(math.floor(len(A)/2)-1, -1, -1):
		maxHeapify(A, i, size)
	
def heapSort(A):
	size = len(A)
	buildMaxHeap(A)
	for i in range(len(A)-1, 0, -1):
		temp = A[0]
		A[0] = A[i]
		A[i] = temp
		size -= 1
		print(A)
		maxHeapify(A, 0, size)

if __name__ == '__main__':
	array = [0,1,2,3,4,5,6]
	heapSort(array)
