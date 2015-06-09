# coding=utf-8
# area.py -- 面積

def area(n, x, y):
	a = x[n - 1] * y[0] - x[0] * y[n - 1]
	for i in range(1, n):
		a += x[i - 1] * y[i] - x[i] * y[i - 1]
	return 0.5 * a

#テスト用
if __name__ == '__main__':
	x = [1, 3, 2, 0 ]
	y = [ 1, 2, 4, 2 ]
	a = area(4, x, y)
	print("面積 = ", a)
	