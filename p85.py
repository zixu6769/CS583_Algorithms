'''
A k-sorted array is when each sum of k element is larger than its predecessor
For example, in a array index as A[0, 10], k = 3, it is said to be k-sorted if:
A[0] + A[1] + A[2] <= A[1] + A[2] + A[3]
A[1] + A[2] + A[3] <= A[2] + A[3] + A[4]
A[2] + A[3] + A[4] <= A[3] + A[4] + A[5] and so on

a) If k = 1, then it is the same as a normal sorted array

b) Example 2-sorted array: [1,3,2,8,100,9]

c) every pair of neighbor k elements have common elements except for first and last.
For example, A[0] + A[1] + A[2] and A[1] + A[2] + A[3].
Both have A[1] and A[2]. To make the second greater than the first,
A[0] must be less than A[3]


'''

if __name__ == '__main__':
	A = [2,8,7,1,3,5,6,4]
	tailQuickSort(A, 0, len(A)-1)
	print(A)
