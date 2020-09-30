from heapSort import *

'''
We can build a heap by repeatedly calling MAX-HEAP-INSERT to insert the elements
into the heap.
'''

def buildMaxHeapPrime(A):
	a = []
	h = Heap(a)
	h.heapSize = 0
	for i in range(0, A.length):
		insertMaxHeap(h, A[i])
	return h

if __name__ == '__main__':
	print("*** Problem 6-1 ***")
	A = [4,1,3,2,16,9,10,14,8,7]
	print("original array     ", A)
	print("they do not produce the same heap!")
	print("buildMaxHeap:      ", buildMaxHeap(Heap(A)))
	print("buildMaxHeapPrime: ", buildMaxHeapPrime(Heap(A)))
	