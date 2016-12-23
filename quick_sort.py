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
	j = 0
	k = len(array)-1
	while(1):
		while(array[pivot] > array[j]):
			j = j + 1
			if j == len(array) - 1:
				break
		while(array[pivot] < array[k]):	
			k = k - 1
			if k == 0:
				break
		if j >= k:
			break
		array = swap(array, j, k)

	array = swap(array, pivot, k)
	return array, k



# quicksort definition starts here
def quick_sort(array):
	n = len(array)
	if n < 3:
		if n == 2 and array[0] > array[1]:
			array = swap(array, 0, 1)
		return array

	# pivot = random.randint(0, n-1)
	# print(pivot)
	pivot = 0
	array, pivot = partition(array, pivot)
	
	# asplitting array into two parts starts here
	split1 = list()
	for i in range(0, pivot):
		split1.append(array[i])

	split2 = list()
	for i in range(pivot+1, n):
		split2.append(array[i])

	# sort the splitted parts recursively
	sorted_split1 = quick_sort(split1)
	sorted_split2 = quick_sort(split2)
	sorted_array = sorted_split1 + [array[pivot]] + sorted_split2

	return sorted_array

#an example set
array = [2,5,4,3,6,0,1,9,8,7]

array = quick_sort(array)
print(array)