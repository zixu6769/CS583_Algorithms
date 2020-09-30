from heapSort import *

'''
Give an O(nlgk) time algorithm to merge k sorted lists into one sorted list,
where n is the total number of elements in all the input lists. (Hint: Use a minheap
for k-way merging.)
'''

# assume lists are sorted increasing order
def mergeList(k, lists):
	if (k < 2):
		raise ValueError('ERROR: not enough lists')

	init = [] # list to hold the first ele from every list
	dictionary = {} # track the origin of each item
	result = []

	# build the initial heap
	for i in range(0, k):
		val = lists[i].pop(0)
		init.append(val)
		dictionary[val] = i
	h = Heap(init)
	buildMinHeap(h)

	# run until no more ele
	while (h.heapSize > 0):
		minVal = extractMin(h)
		result.append(minVal)
		if (len(lists[dictionary[minVal]]) != 0):
			nextVal = lists[dictionary[minVal]].pop(0)
			insertMinHeap(h, nextVal)
			dictionary[nextVal] = dictionary[minVal]
	return result

if __name__ == '__main__':
	# the method doesn't work if lists contatins duplicate items
	lists = [[1,2,6,7,8], [15,44,73,934], [0,23,56,99,1000]]
	print(mergeList(3, lists))