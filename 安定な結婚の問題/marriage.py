# coding=utf-8
#	marriage.py -- 安定な結婚の問題

boy = []
girl = []
position = []
rank = [];

def init(n):
	tmp1 =  [0 for i in range(n + 1)]
	tmp2 =  [(n + 1) for i in range(n + 1)]
	for i in range(n + 1):
		boy.append(0)
		girl.append(tmp1)
		position.append(0)
		rank.append(tmp2)

def setGirl(g, n):
	print("女", g, ":")
	for r in range(1, n + 1):
		b = int(input())
		rank[g][b] = r

def setBoy(b, n):
	print("男", b, ":")
	for r in range(1, n + 1):
		g = int(input())
		girl[b][r] = g

def calc(n):
	for b in range(1, n + 1):
		s = b;
		while (s != 0):
			position[s] += 1
			g = girl[s][position[s]]
			if (rank[g][s] < rank[g][boy[g]]) :
				t = boy[g]
				boy[g] = s
				s = t

def printresult(n):
	for g in range(1, n + 1):
		print("女 ", g, " - 男 ", boy[g])

#テスト用
if __name__ == '__main__':
	n = 3		# 各性の人数
	init(n)

	for g in range(1, n + 1):	#各女性の好み
		setGirl(g, n)

	for b in range(1, n + 1):	#各男性の好み 
		setBoy(b, n)

	calc(n)
	printresult(n)
