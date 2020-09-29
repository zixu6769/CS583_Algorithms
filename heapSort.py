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
	
def heapSort(A):
	buildMaxHeap(A)
	for i in range(A.length - 1, 0, -1):
		temp = A[0]
		A[0] = A[i]
		A[i] = temp
		A.heapSize -= 1
		maxHeapify(A, 0)
	return A

# assume A is max heap
def maximum(A):
	return A[0]

# assume A is max heap
def extractMax(A):
	if (A.heapSize < 1):
		raise ValueError('ERROR: heap underflow')
	maxVal = A[0]
	A[0] = A[A.heapSize - 1]
	A.heapSize -= 1
	maxHeapify(A, 0)
	return maxVal

# assume A is max heap
def increaseKey(A, i, key):
	if (key < A[i]):
		raise ValueError('ERROR: new key is smaller than current key')
	A[i] = key
	while (i > 0 and A[A.parent(i)] < A[i]):
		temp = A[i]
		A[i] = A[A.parent(i)]
		A[A.parent(i)] = temp
		i = A.parent(i)

# assume A is max heap
def insert(A, key):
	A.heapSize += 1
	A.insert(A.heapSize-1, -math.inf)
	increaseKey(A, A.heapSize-1, key)

#******** Problem 6-1 ********#
def buildMaxHeapPrime(A):
	a = []
	h = Heap(a)
	h.heapSize = 0
	for i in range(0, A.length):
		insert(h, A[i])
	return h

if __name__ == '__main__':
	A1 = [4,1,3,2,16,9,10,14,8,7] # textbook page 161
	print("*** test1 ***")
	print("original array ", A1)
	print("sorted array   ", heapSort(Heap(A1)))
	print("")

	print("*** test2 ***")
	A2 = [5,1,99,23,15]
	h2 = Heap(A2)
	buildMaxHeap(h2)
	print("original heap ", h2)
	print("max value: ", maximum(h2))
	print("size: ", h2.heapSize)
	print("Extracting ", extractMax(h2), "...")
	print("new size: ", h2.heapSize)
	print("")

	print("*** test3 ***")
	A3 = [0,1,2,3,4,5,6]
	h3 = Heap(A3)
	buildMaxHeap(h3)
	print("original heap ", h3)
	print("increasing value 2 to 12 ...")
	increaseKey(h3, 6, 12)
	print("new heap: ", h3)
	print("inserting 50 ...")
	insert(h3, 50)
	print("new heap: ", h3)

	print("*** Problem 6-1 ***")
	A4 = [4,1,3,2,16,9,10,14,8,7]
	h4 = Heap(A4)
	buildMaxHeap(h4)
	print("original array     ", A4)
	print("buildMaxHeap:      ", h4)
	h4 = Heap(A4)
	print("buildMaxHeapPrime: ", buildMaxHeapPrime(h4))