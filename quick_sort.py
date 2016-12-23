import random
import sys
import os

# swap definition
def swap(array, j, k):
	temp = array[j]
	array[j] = array[k]
	array[k] = temp
	return array

# partition definition
def partition(array, pivot):
	array = swap(array, 0, pivot)
	pivot = 0
	i = 1
	for j in range(0, len(array)):
		if array[j] < array[pivot]:
			array = swap(array, j, i)
			i = i + 1
	array = swap(array, pivot, i-1)
	return array, i-1

# quicksort definition starts here
def quick_sort(array):
	n = len(array)
	if n <= 1:
		return array
	pivot = random.randint(0, n-1)
	array, pivot = partition(array, pivot)
	# splitting array into two parts starts here
	split1 = list()
	split2 = list()
	for i in range(0, n):
		if i<pivot:
			split1.append(array[i])
		if i > pivot:
			split2.append(array[i])
	# sort the splitted parts recursively and return
	return quick_sort(split1) + [array[pivot]] + quick_sort(split2)

#an example set
array = [24, 12,16,9,5,4,23,18,14,1,10,17,2,13,3,11,21,6,25,7,22,15,19,20,8]
array = quick_sort(array)
print(array)