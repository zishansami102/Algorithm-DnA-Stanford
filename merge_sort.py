import random
import sys
import os


def mergesort(A):
	n = len(A)
	if n==1:
		return A

	B = list()
	for i in range( 0, n//2):
		B.append(A[i])


	C = list()
	for i in range(n//2, n):
		C.append(A[i])


	if n > 2:
		B = mergesort(B)
		C = mergesort(C)
	j = 0
	k = 0
	D = list()
	for i in range( 0, n):
		if j < len(B) and k < len(C):
			if B[j]<C[k]:
				D.append(B[j])
				j = j + 1
			else:
				D.append(C[k])
				k = k + 1
		else:
			if k >= len(C) and j < len(B):
				D.append(B[j])
				j = j + 1
			else:
				D.append(C[k])
				k = k + 1
	return D

array = [24, 12,16,9,5,4,23,18,14,1,10,17,2,13,3,11,21,6,25,7,22,15,19,20,8]
sorted = mergesort(array)

for element in sorted:
	print(element)

