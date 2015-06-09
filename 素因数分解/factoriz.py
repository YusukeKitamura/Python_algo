# coding=utf-8
#	factoriz.py -- �f��������

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
	
# �e�X�g
for i in range(1, 101):
	factorize(i)
	