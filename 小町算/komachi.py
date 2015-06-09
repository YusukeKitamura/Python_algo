# coding=utf-8
#	komachi.c -- 小町算

def komachi():
	sign = [-1] * 10

	for i in range(1, 10):
		sign[i] = -1
		
	while True:
		x = n = 0
		s = 1
		for i in range(1, 10):
			if (sign[i] == 0) :
				n = 10 * n + i
			else :
				x += s * n
				s = sign[i]
				n = i
		x += s * n
		if (x == 100):
			for i in range(1, 10):
				if (sign[i] ==  1):
					print(" + ",  end="");
				elif (sign[i] == -1):
					print(" - ",  end="");
				print(i,  end="")
			print(" = 100")
		i = 9
		s = sign[i] + 1
		while (s > 1):
			sign[i] = -1
			i -= 1
			s = sign[i] + 1
		sign[i] = s
		if (sign[1] >= 1):
			break

#テスト用
if __name__ == '__main__':
	komachi()
