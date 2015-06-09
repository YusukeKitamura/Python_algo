# coding=utf-8
#	ishi1.py -- 石取りゲーム 1

def ishi1(n, m):
	my_turn = 1
	
	while n > 0 :
		if my_turn == 1:
			x = (n - 1) % (m + 1)
			if x == 0:
				x = 1
				print("私は ", x, " 個の石を取ります.")
		else:
			while True:
				print("何個取りますか? ");
				x = int(input())
				if (x > 0 and x <= m and x <= n):
					break
		n -= x
		print("残りは ", n, " 個です.")
		my_turn = 1 - my_turn
	
	return my_turn
	
#テスト用
if __name__ == '__main__':
	print("最後に石を取った側が負けです. パスはできません.")
	print("石の数? ")
	n = int(input())
	print("１回に取れる最大の石の数? ")
	m = int(input())
	
	lose = ishi1(n, m)
	
	if (lose == 1):
		print("あなたの負けです!")
	else:
		print("私の負けです!")
