# coding=utf-8
#	normal.c -- 正規分布
import math

PI  = 3.14159265358979323846264

# 正規分布の下側確率
def p_nor(z):
	z2 = z * z
	t = p = z * math.exp(-0.5 * z2) / math.sqrt(2.0 * PI)
	for i in range(3, 200, 2):
		prev = p
		t *= z2 / i
		p += t
		if (p == prev):
			return 0.5 + p
	if (z > 0):
		return 1
	else:
		return 0

#  正規分布の上側確率
def q_nor(z):
	return 1 - p_nor(z)

#テスト用
if __name__ == '__main__':
	print("正規分布の下側確率")
	for i in range(0, 21):
		z = 0.2 * i
		print(round(z, 1), " ", p_nor(z))
