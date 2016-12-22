import random
import sys
import os

def dist(p, q):
	distance = ((p[0]-q[0])**2 + (p[1]- q[1])**2)**(1/2)
	return distance

def sort_x(pset):
	n = len(pset)
	if n==1:
		return pset
#splitting in two parts
	B = list()
	for i in range( 0, n//2):
		B.append(pset[i])

	C = list()
	for i in range(n//2, n):
		C.append(pset[i])
# sorting the splitted parts
	if n > 2:
		B = sort_x(B)
		C = sort_x(C)
#merging the splitted parts
	j = 0
	k = 0
	D = list()
	for i in range( 0, n):
		if j < len(B) and k < len(C):
			if B[j][0]<C[k][0]:
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


def sort_y(pset):
	n = len(pset)
	if n==1:
		return pset
#splitting in two parts
	B = list()
	for i in range( 0, n//2):
		B.append(pset[i])

	C = list()
	for i in range(n//2, n):
		C.append(pset[i])
# sorting the splitted parts
	if n > 2:
		B = sort_y(B)
		C = sort_y(C)
#merging the splitted parts
	j = 0
	k = 0
	D = list()
	for i in range( 0, n):
		if j < len(B) and k < len(C):
			if B[j][1]<C[k][1]:
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

def closest_split_pair( px, py, delta):
	n = len(px)
	x_mid = px[n//2][0]
	sy = list()
	for i in range(0, n):
		if (py[i][0] >= x_mid-delta) and (py[i][0] <= x_mid+delta):
			sy.append(py[i])
	best = delta
	best_pair = None
	for i in range(1, len(sy)-1):
		loop_end = min(7, len(sy)-i)
		for j in range(1, loop_end):
			p = sy[i]
			q = sy[i+j]
			distance = dist(p, q)
			if distance < best:
				best_pair = (p, q)
				best = distance
	return best_pair

def closest_pair(px, py):
	n = len(px)
	if n==2:
		return px[0], px[1]
	if n==3:
		d1 = dist(px[0], px[1])
		d2 = dist(px[0], px[2])
		d3 = dist(px[1], px[2])
		if min(d1, d2, d3) == d1:
			return px[0], px[1]
		if min(d1, d2, d3) == d2:
			return px[0], px[2]
		if min(d1, d2, d3) == d3:
			return px[1], px[2]

	qx = list()
	for i in range(0, n//2):
		qx.append(px[i])
	qy = sort_y(qx)

	rx = list()
	for i in range(n//2, n):
		rx.append(px[i])
	ry = sort_y(rx)

	p1, q1 = closest_pair(qx, qy)
	p2, q2 = closest_pair(rx, ry) 
	d1 = dist(p1, q1)
	d2 = dist(p2, q2)
	best_pair = closest_split_pair(px, py, min(d1, d2))
	if best_pair == None:
		if d1>d2:
			return p1, q1
		else:
			return p2, q2
	else:
		return best_pair


point_set = [[5,3],[7,12],[3,5],[12,7],[6,6],[5,5]]
px = sort_x(point_set)
py = sort_y(point_set)
p1, p2 = closest_pair(px, py)
print(p1, p2)

