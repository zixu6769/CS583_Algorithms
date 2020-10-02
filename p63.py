import math

# Young tableaus
class Table(list):
	def __init__(self, A, m, n):
		super().__init__(A)
		self.length = m * n
		self.tableSize = 0
		self.m = m
		self.n = n

	def left(self, i):
		return i - 1

	def right(self, i):
		return i + 1

	def up(self, i):
		return i - self.m

	def down(self, i):
		return i + self.m

def minTablefy(A, i):
	r = A.right(i)
	d = A.down(i)
	if (r <= A.tableSize-1 and A[r] < A[i]):
		smallest = r
	else:
		smallest = i
	if (d <= A.tableSize-1 and A[d] < A[smallest]):
		smallest = d
	if (smallest != i):
		temp = A[i]
		A[i] = A[smallest]
		A[smallest] = temp
		minTablefy(A, smallest)

def buildMinTable(A):
	A.tableSize = len(A)
	for i in range(A.tableSize - 1, -1, -1):
		minTablefy(A, i)
	for i in range(A.tableSize, A.length):
		A.append(math.inf)

'''
worst case is the table is full (no inf)
so when we change A[0] to inf, it has to move all the way to the last pos
which is m + n - 2 moves, each move takes constant time
thus the run time is bounded by O(m + n)
'''
def extractMin(A):
	if (A.tableSize < 1):
		raise ValueError('ERROR: table empty')
	minVal = A[0]
	A[0] = math.inf
	minTablefy(A, 0)
	A.tableSize -= 1
	return minVal

def decreaseElement(A, i, value):
	if (A[i] < value):
		raise ValueError('ERROR: new value is greater than current')
	A[i] = value
	
	while (True):
		largerParent = -1
		if (A.left(i) >= 0 and A[A.left(i)] > A[i]):
			largerParent = A.left(i)
		if (A.up(i) >= 0 and A[A.up(i)] > A[largerParent]):
			largerParent = A.up(i)
		if(largerParent == -1):
			break
		else:
			temp = A[i]
			A[i] = A[largerParent]
			A[largerParent] = temp
			i = largerParent

'''
worst case is the new element is the smallest and in the last position
each swap takes constant time, there are m + n - 2 swaps
thus the run time is bounded by O(m + n)
'''
def insert(A, element):
	if (A.tableSize == A.length):
		raise ValueError('ERROR: table full')
	A.tableSize += 1
	decreaseElement(A, A.tableSize-1, element)

'''
step 1: build a empty table, and insert all element from A.
		Each insert takes O(2n), there are n*2 elements, so O(n*3)
step 2: extractMin until the table is empty.
		Each extract takes O(2n), there are n*2 elements, so O(n*3)
Thus the run time is bounded by O(n*3)
'''
def tableSort(A, n):
	t = Table([], n, n)
	result = []
	for i in range(0, t.length):
		t.append(math.inf)
	for element in A:
		insert(t, element)
	for i in range(0, t.tableSize):
		result.append(extractMin(t))
	return result

'''
keep finding the closer grid to the target value, 
stop when target is found or it doesn't exist.
Worst case is the target value is at the last pos, 
which requires (m + n - 3) steps, each takes constant time,
Thus the run time is bounded by O(m + n)
'''
def contains(A, i, value):
	r = A.right(i)
	d = A.down(i)
	if (A[r] == value or A[d] == value or A[i] == value): return True
	if (A[r] > value and A[d] > value): return False
	if (A[r] < value): closest = r
	if (A[d] < value and ((value - A[d]) < (value - A[r]))): closest = d
	return contains(A, closest, value)


if __name__ == '__main__':
	A = [9,16,3,2,4,8,5,14,12]
	print(tableSort(A, 4))
	t = Table(A, 4, 4)
	buildMinTable(t)
	print(contains(t, 0, 17))
