# coding=utf-8
# gencomb.py -- 組合せの生成

def first(n):
	return (1 << n) - 1

def nextset(x):
	smallest = x & -x
	ripple = x + smallest
	new_smallest = ripple & -ripple
	ones = ((int(new_smallest / smallest)) >> 1) - 1
	return ripple | ones

def printset(s, N):
	for i in range(1, N+1):
		if (s & 1):
			print(" ", i, end="")
		s >>= 1
	print(" ")

print("N:")
N = int(input())
if (N < 1) :
	print("N is more than 0 !")
	exit()

print("K:")
K = int(input())
if (K < 1 or K > N) :
	print("K is more than 0!")
	print("K is not bigger than N!")
	exit()

#テスト用
if __name__ == '__main__':
	i = 1
	x = first(K)

	while (not (x & ~first(N) ) ) :
		print(repr(i).rjust(4), ":", end="")
		printset(x, N)
		x = nextset(x)
		i += 1
