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

# choose pivot definition for Dselect
def choose_pivot(array):
	if len(array)==1:
		return 0
	if len(array)%5==0:
		t = len(array)//5
	else:
		t = len(array)//5 + 1
	d = [[] for i in range(t)]
	k = 0
	for j in range(0,len(array)):
		d[k].append(array[j])
		if (j+1)%5==0 :
			k = k+1
	m = []
	for j in range(0, t):
		d[j].sort()
		m.append(d[j][len(d[j])//2])
	med = Dselect(m, t//2)
	for j in range(len(array)):
		if array[j] == med:
			return j


# Dselect definition starts here
def Dselect(array, i):
	pivot = choose_pivot(array)
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
	return Dselect(split, new_i)

a = [24,0,12,16,9,5,4,23,18,14,1,10,17,2,13,3,11,21,6,25,7,22,15,19,20,8]
print(Rselect(a, 3))

print(Dselect(a, 9))
print(Dselect(a, 25))

