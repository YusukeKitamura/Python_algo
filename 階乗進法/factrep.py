# coding=utf-8
#	factrep.py -- �K��i�@

# 0 ���� (n + 1)! - 1 �܂ł̐������K��i�@�ŏ����o��
def factrep(n):
	c = [0] * (n + 2)

	i = 0
	while True:
		print(i, ":", end="")
		i += 1
		for k in range(n, 0, -1):
			print(" ", c[k], end="")
		
		print("")
		k = 1
		while (c[k] == k):
			c[k] = 0
			k += 1
			
		c[k] += 1
		if (k > n):
			break
	
#�e�X�g�p
if __name__ == '__main__':
	N = 4
	factrep(N)
