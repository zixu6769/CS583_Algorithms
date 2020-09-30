from heapSort import *

'''
Each exchange operation on line 5 of HEAP-INCREASE-KEY typically requires
three assignments. Show how to use the idea of the inner loop of INSERTIONSORT
to reduce the three assignments down to just one assignment.
'''

def increaseKeyPrime(A, i, key):
	if (key < A[i]):
		raise ValueError('ERROR: new key is smaller than current key')

	while (i > 0 and A[A.parent(i)] < key):
		A[i] = A[A.parent(i)]
		i = A.parent(i)
	A[i] = key