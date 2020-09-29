import math

class Heap:
	def __init__(self, array):
		self.array = array

	def parent(self, i):
		return self.array[math.floor((i-1)/2)]

	def left(self, i):
		return self.array[2*i + 1]

	def right(self, i):
		return self.array[2*i + 2]

def maxHeapify()


def heapSort(array):
	h = Heap(array)
