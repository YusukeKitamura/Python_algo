# coding=utf-8
#	ishi2.py -- 石取りゲーム 2

def ishi2(n):
	f = [0, 1]
	for i in range(20): 
		f.append(f[i] + f[i + 1])
		
	max = n - 1
	my_turn = 1
	while n > 0 :
		print(max, " 個まで取れます.")
		if (my_turn == 1):
			x = n
			i = 20
			while(x != f[i]):
				if (x > f[i]):
					x -= f[i]
				i -= 1
			if (x > max):
				x = 1
			print("私は ", x, " 個の石をとります.")
		else:
			while True:
				print("何個とりますか? ");
				x = int(input())
				if (x >= 0 and x <= max):
					break
		
		n -= x
		max = 2 * x
		if (max > n):
			max = n;
		print("残りは ", n, " 個です.")
		my_turn = 1 - my_turn
		
	return my_turn

#テスト用
if __name__ == '__main__':
	print("石の数 (2..10000)? ")
	n = int(input())
	
	win = ishi2(n)
	
	if (win == 1):
		print("あなたの勝ちです!")
	else:
		print("私の勝ちです!")
