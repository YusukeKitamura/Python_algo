# coding=utf-8
#	radconv.py -- 基数の変換
import sys

def conv1(x, d, m, c):
	for i in range(0, m):
		if x == 0:
			break
		c.append(x % d) 
		x = int(x/d)
	
	if (x == 0):
		return i  # 桁数 
	else:
		return -1  # エラー 
		

def conv2(d1, m1, x1, d2, m2, x2):
	for i in range(0, m2):
		if m1 <= 0:
			break
		r = 0
		for j in range(m1-1, -1, -1):
			t = d1 * r + x1[j]
			x1[j] = int(t / d2)
			r = t % d2
			
		x2.append(r)
		while (m1 > 0 and x1[m1 - 1] == 0):
			m1 -= 1
			
	if (m1 == 0):
		return i		 # 桁数 
	else:
		return -1 	# エラー 

M = 1000

print("x = ")
x = int(input())

x1 = []
m1 = conv1(x, 8, M, x1)
if (m1 < 0) :
	print("conv1: error")
	sys.exit()

print("8進(octal): ",  end="")
for i in range(m1-1, -1, -1):
	print(x1[i], end="")
print(" ")

x2 = []
m2 = conv2(8, m1, x1, 2, M, x2)
if (m1 < 0) :
	print("conv2: error")
	sys.exit()

print("2進(binary): ",  end="")
for i in range(m2-1, -1, -1):
	print(x2[i],  end="")
