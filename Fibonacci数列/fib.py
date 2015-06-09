# coding=utf-8
#	fib.py -- Fibonacci (�t�B�{�i�b�`) ����
import math

# ��ʍ��𒼐ڌv�Z������@
def fib1(n):
	return math.floor(pow((1 + math.sqrt(5)) / 2, n)/ math.sqrt(5) + 0.5)

# �s��̗ݏ�v�Z��W�J���Čv�Z���AO(log n)�ŋ��߂���@
def fib2(n):
	a = 1
	b = 1
	c = 0
	x = 1
	y = 0
	n = n - 1
	while math.floor(n) > 0:
		if n % 2 == 1:
			x1 = x
			y1 = y
			x = a * x1 + b * y1
			y = b * x1 + c * y1

		n = math.floor(n / 2)
		a1 = a
		b1 = b
		c1 = c
		a = a1 * a1 + b1 * b1
		b = b1 * (a1 + c1)
		c = b1 * b1 + c1 * c1
	return x

# ��`����ċA�Ōv�Z����BO(2^n)
def fib3(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib3(n - 1) + fib3(n - 2)

# ���I�v��@�Ōv�Z����BO(n)
def fib4(n):
	fiblist = [0, 1]
	if n >= 2:
		for i in range(1, n):
			newval = fiblist[i] + fiblist[i-1]
			fiblist.append(newval)
	return fiblist[n]

	
for n in range(1, 12):
	print(fib1(n), " ", end="")

print()
	
for n in range(1, 12):
	print(fib2(n), " ", end="")

print()

for n in range(1, 12):
	print(fib3(n), " ", end="")

print()

for n in range(1, 12):
	print(fib4(n), " ", end="")
