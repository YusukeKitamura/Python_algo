# coding=utf-8
#	fukumen.py -- 覆面算
import sys

N = 10  # 最大の行数

imax = 0
jmax = 0
solution = 0
word = [[0]*N]*128
digit = [0]*256
low = [0]*256
ok = [1]*10

def found():  #解の表示
	global imax
	global jmax
	global solution
	solution += 1
	print("\n解 ", solution)
	for i in range(0, imax+1):
		for j in range(jmax, -1, -1):
			c = word[i][j]
			if (c != '\0'):
				print(digit[ord(c)], end="")
			else:
				print(" ", end="")
		print(" ")
	
def search(sum, i, j):  # 再帰的に試みる
	c = word[i][j]
	print(c)
	if (i < imax):
		d = digit[ord(c)]
		if (d < 0):  # 定まっていないなら 
			for d in range(low[ord(c)], 10):
				if ok[d]:
					digit[ord(c)] = d
					ok[d] = 0
					search(sum + d, i + 1, j)
					ok[d] = 1
			digit[ord(c)] = -1;
		else:
			search(sum + d,  i + 1, j)
	else:
		d = sum % 10
		carry = sum / 10
		if (digit[ord(c)] == d):
			if (j <= jmax):
				search(carry, 0, j + 1)
			elif (carry == 0):
				found()
		elif (digit[ord(c)] < 0 and ok[d] and d >= low[ord(c)]):
			digit[ord(c)] = d
			ok[d] = 0
			if (j <= jmax):
				search(carry, 0, j + 1)
			elif (carry == 0):
				found()
			digit[ord(c)] = -1
			ok[d] = 1
			
def set():
	for i in range(0, min(N+1, imax+1)):
		print(i + 1, ":")
		buffer = input()
		low[ord(buffer[0])] = 1
		k = len(buffer) - 1
		global jmax
		if (k > jmax):
			jmax = k;
		for j in range(0, k+1):
			c = word[i][j] = buffer[k - j]
			if (c.isalpha()):
				digit[ord(c)] = -1
			elif (c.isdigit()):
				digit[ord(c)] = c - '0'

#テスト用
if __name__ == '__main__':
	print("行数? ")
	global imax
	imax = int(input())
	imax -= 1
	set()
	search(0, 0, 0)
	if (solution == 0):
		print("解はありません.")
