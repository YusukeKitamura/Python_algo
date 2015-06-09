# coding=utf-8
#	inssort.py -- ‘}“üƒ\[ƒg

# a[0..n-1] ‚ğ¸‡‚É
def inssort(n, a) :
	for i in range(1, n):
		x = a[i]
		for j in range(i-1, -1, -1):
			if (a[j] <= x):
				break
			a[j + 1] = a[j]
		a[j + 1] = x

if __name__ == '__main__':
	import random
	N = 20
	a = [0]*N

	print("Before:");
	for i in range(0, N):
		a[i] = random.randint(0, 100)
		print(a[i], " ", end="")
		
	print("\n")
	inssort(N, a)
	print("After: ")
	for i in range(0, N):
		print(a[i], " ", end="")
		