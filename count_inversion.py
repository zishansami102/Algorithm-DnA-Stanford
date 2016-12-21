import random
import sys
import os


def sort_and_count(A):
	n = len(A)
	if n==1:
		return A, 0
#splitting in two parts
	B = list()
	for i in range( 0, n//2):
		B.append(A[i])

	C = list()
	for i in range(n//2, n):
		C.append(A[i])
# sorting the splitted parts
	l_inv = 0
	r_inv = 0
	if n > 2:
		B, l_inv = sort_and_count(B)
		C, r_inv = sort_and_count(C)
#merging the splitted parts
	j = 0
	k = 0
	split_inv = 0
	D = list()
	for i in range( 0, n):
		if j < len(B) and k < len(C):
			if B[j]<C[k]:
				D.append(B[j])
				j = j + 1
			else:
				D.append(C[k])
				k = k + 1
				split_inv = split_inv + len(B) - j
		else:
			if k >= len(C) and j < len(B):
				D.append(B[j])
				j = j + 1
			else:
				D.append(C[k])
				k = k + 1
	tot_inv = l_inv + r_inv + split_inv
	return D, tot_inv

array = [6,5,4,3,2,1]
sorted, inv = sort_and_count(array)
print(inv)

