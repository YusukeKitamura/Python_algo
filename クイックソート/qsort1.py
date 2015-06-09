# coding=utf-8
#	qsort1.py -- クイックソート

def quicksort(a, first, last):
	x = a[int((first + last) / 2)]
	i = first
	j = last
	while 1:
		while (a[i] < x):
			i += 1
		while (x < a[j]):
			j -= 1
		if (i >= j):
			break
		t = a[i]
		a[i] = a[j]
		a[j] = t
		i += 1
		j -= 1
	if (first  < i - 1):
		quicksort(a, first , i - 1)
	if (j + 1 < last):
		quicksort(a, j + 1, last)

if __name__ == '__main__':
	import random
	N = 20
	a = [0]*N

	print("Before:")
	for i in range(0, N):
		a[i] = random.randint(0, 100)
		print(a[i], " ", end="")
		
	print("\n")
	quicksort(a, 0, N - 1)
	print("After: ")
	for i in range(0, N):
		print(a[i], " ", end="")
	