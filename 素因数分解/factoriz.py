# coding=utf-8
#	factoriz.py -- 素因数分解

def factorize(x):
	print(x, " = ", end="")
	while (x >= 4 and x % 2 == 0):
		print("2 * ", end="")
		x /= 2
		
	d = 3
	q = x / d
	while q >= d:
		if x % d == 0:
			print(d, "* ", end="")
			x = q
		else:
			d += 2
		q = x / d
		
	print(int(x))
	
# テスト
for i in range(1, 101):
	factorize(i)
	