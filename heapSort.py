import math

# binary heap
class Heap(list):
	def __init__(self, A):
		super().__init__(A)
		self.length = len(A)
		self.heapSize = 0

	def parent(self, i):
		return math.floor((i-1)/2)

	def left(self, i):
		return 2*i + 1

	def right(self, i):
		return 2*i + 2

#-------------- Max Heap Methods --------------#
def maxHeapify(A, i):
	l = A.left(i)
	r = A.right(i)
	if (l <= A.heapSize-1 and A[l] > A[i]):
		largest = l
	else:
		largest = i
	if (r <= A.heapSize-1 and A[r] > A[largest]):
		largest = r
	if (largest != i):
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		maxHeapify(A, largest)

def buildMaxHeap(A):
	A.heapSize = A.length
	for i in range(math.floor(A.length/2)-1, -1, -1):
		maxHeapify(A, i)
	return A
	
def maxHeapSort(A):
	buildMaxHeap(A)
	for i in range(A.length - 1, 0, -1):
		temp = A[0]
		A[0] = A[i]
		A[i] = temp
		A.heapSize -= 1
		maxHeapify(A, 0)
	return A

def maximum(A):
	return A[0]

def extractMax(A):
	if (A.heapSize < 1):
		raise ValueError('ERROR: heap underflow')
	maxVal = A[0]
	A[0] = A[A.heapSize - 1]
	A.heapSize -= 1
	maxHeapify(A, 0)
	return maxVal

def increaseKey(A, i, key):
	if (key < A[i]):
		raise ValueError('ERROR: new key is smaller than current key')
	A[i] = key
	while (i > 0 and A[A.parent(i)] < A[i]):
		temp = A[i]
		A[i] = A[A.parent(i)]
		A[A.parent(i)] = temp
		i = A.parent(i)

def insertMaxHeap(A, key):
	A.heapSize += 1
	A.insert(A.heapSize-1, -math.inf)
	increaseKey(A, A.heapSize-1, key)

#-------------- Min Heap Methods--------------#
def minHeapify(A, i):
	l = A.left(i)
	r = A.right(i)
	if (l <= A.heapSize-1 and A[l] < A[i]):
		smallest = l
	else:
		smallest = i
	if (r <= A.heapSize-1 and A[r] < A[smallest]):
		smallest = r
	if (smallest != i):
		temp = A[i]
		A[i] = A[smallest]
		A[smallest] = temp
		minHeapify(A, smallest)

def buildMinHeap(A):
	A.heapSize = A.length
	for i in range(math.floor(A.length/2)-1, -1, -1):
		minHeapify(A, i)
	
def minHeapSort(A):
	buildMinHeap(A)
	for i in range(A.length - 1, 0, -1):
		temp = A[0]
		A[0] = A[i]
		A[i] = temp
		A.heapSize -= 1
		minHeapify(A, 0)
	return A

def minimum(A):
	return A[0]

def extractMin(A):
	if (A.heapSize < 1):
		raise ValueError('ERROR: heap underflow')
	minVal = A[0]
	A[0] = A[A.heapSize - 1]
	A.heapSize -= 1
	minHeapify(A, 0)
	return minVal

def decreaseKey(A, i, key):
	if (key < A[i]):
		raise ValueError('ERROR: new key is greater than current key')
	A[i] = key
	while (i > 0 and A[A.parent(i)] > key):
		A[i] = A[A.parent(i)]
		i = A.parent(i)
	A[i] = key

def insertMinHeap(A, key):
	A.heapSize += 1
	A.insert(A.heapSize-1, math.inf)
	decreaseKey(A, A.heapSize-1, key)

if __name__ == '__main__':
	A = [4,1,3,2,16,9,10,14,8,7] # textbook page 161
	print("original array ", A)
	print("maxHeapSort:", maxHeapSort(Heap(A)))
	print("mimHeapSort:", minHeapSort(Heap(A)))