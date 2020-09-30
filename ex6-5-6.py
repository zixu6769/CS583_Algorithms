from heapSort import *

def increaseKeyPrime(A, i, key):
	if (key < A[i]):
		raise ValueError('ERROR: new key is smaller than current key')

	while (i > 0 and A[A.parent(i)] < key):
		A[i] = A[A.parent(i)]
		i = A.parent(i)
	A[i] = key