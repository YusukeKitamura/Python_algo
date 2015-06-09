# coding=utf-8
#	bubsort.py -- バブルソート

def bubblesort(n, a):
	k = n - 1
	while (k >= 0):
		j = -1
		for i in range(1, k + 1):
			if (a[i - 1] > a[i]) :
				j = i - 1
				x = a[j]
				a[j] = a[i]
				a[i] = x
		k = j

if __name__ == '__main__':
	import random
	N = 20
	a = [0]*N

	print("Before:");
	for i in range(0, N):
		a[i] = random.randint(0, 100)
		print(a[i], " ", end="")
		
	print("\n")
	bubblesort(N, a)
	print("After: ")
	for i in range(0, N):
		print(a[i], " ", end="")
		