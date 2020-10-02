import math

# d-ary heap
# height is log(d)n
class Heap(list):
	def __init__(self, A, d):
		super().__init__(A)
		self.length = len(A)
		self.heapSize = 0
		self.d = d

	def parent(self, i):
		return math.floor((i-1)/self.d)

	# return index of kth child of node index at i
	def child(self, i, k):
		return self.d * i + k

#-------------- Max Heap Methods --------------#
def maxHeapify(A, i):
	largest = i
	for k in range (1, A.d+1):
		index = A.child(i, k)
		if (index <= A.heapSize-1 and A[index] > A[largest]):
			largest = index
	if (largest != i):
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		maxHeapify(A, largest)

def buildMaxHeap(A):
	A.heapSize = A.length
	for i in range(math.floor(A.length/A.d) - 1, -1, -1):
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
	A.pop()
	maxHeapify(A, 0) 
	return maxVal

# O(logdn)
def increaseKey(A, i, key):
	if (key < A[i]):
		raise ValueError('ERROR: new key is smaller than current key')
	A[i] = key
	while (i > 0 and A[A.parent(i)] < A[i]):
		temp = A[i]
		A[i] = A[A.parent(i)]
		A[A.parent(i)] = temp
		i = A.parent(i)

# O(logdn)
def insertMaxHeap(A, key):
	A.heapSize += 1
	A.insert(A.heapSize-1, -math.inf)
	increaseKey(A, A.heapSize-1, key)

if __name__ == '__main__':
	A = [0,1,2,3,4,5,6,7,8,9,10,11,12]
	h = Heap(A,3)
	buildMaxHeap(h)
	print(h)
	print(insertMaxHeap(h, 100))
	print(h)
