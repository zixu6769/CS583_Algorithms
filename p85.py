'''
Tail-Recursive-Quicksort
Instead of calling quicksort on the right array,
it simply update the p value to the first element in the right array
which is essentially the same functionality
'''

'''
stack depth is Theta(n) if the right part has size 0
that is when p >= r, so for example [1,2,3,4,5]
'''
def tailQuickSort(A, p, r):
	while (p < r):
		q = partition(A, p ,r)
		tailQuickSort(A, p, q - 1)
		p = q + 1

def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if (A[j] <= x):
			i += 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[i + 1]
	A[i + 1] = A[r]
	A[r] = temp
	return i + 1


if __name__ == '__main__':
	A = [2,8,7,1,3,5,6,4]
	tailQuickSort(A, 0, len(A)-1)
	print(A)
