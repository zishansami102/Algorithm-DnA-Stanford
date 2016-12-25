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

# Rselect definition starts here
def Rselect(array, i):
	pivot = random.randint(0, len(array)-1)
	array, pivot = partition(array, pivot)
	if pivot == i:
		return array[i]
	split = []
	if pivot > i:
		for j in range(0, pivot):
			split.append(array[j])
		new_i = i
	if pivot < i:
		for j in range(pivot+1, len(array)):
			split.append(array[j])
		new_i = i - pivot - 1
	return Rselect(split, new_i)

a = [5,3,4,8,6,1,2,0]
print(Rselect(a, 3))