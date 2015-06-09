# coding=utf-8
#	hanoi.py -- ハノイの塔

def movedisk(n, a, b):
	if (n > 1):
		movedisk(n - 1, a, 6 - a - b)
	print("円盤 ", n,	" を ", a," から ", b, " に移す")
	if (n > 1):
		movedisk(n - 1, 6 - a - b, b)

# テスト
if __name__ == '__main__':
	print("円盤の枚数? ")
	n = int(input())

	print("円盤 ", n, " 枚を柱 1 から柱 2 に移す方法は")
	print("次の ",(1 << n) - 1," 手です.")

	movedisk(n, 1, 2)
