# coding=utf-8
#	kmp.py -- Knuth--Morris--Pratt法
import sys, string

def position(text, pattern):
	tLen = len(text)
	pLen = len(pattern)
	next = [0] * (pLen + 1)

	if (len(pattern) == 0):
		return 0
	i = 1
	j = 0
	next[1] = 0
	while (i < pLen):
		if (pLen > tLen):
			print("pattern が長過ぎます！")
			return -1		# エラー: {\tt pattern}が長すぎる
		if (pattern[i] == pattern[j]):
			i += 1
			j += 1
			next[i] = j
		elif (j == 0):
			i += 1
			next[i] = j
		else:
			j = next[j]
			
	for j in range(0, pLen):
		print("pattern[", j, "] = ", pattern[j], "next[", j + 1, "] = ", next[j + 1])
	i = j = 0
	while (i < tLen and j < pLen):
		if (text[i] == pattern[j]):
			i += 1
			j += 1
		elif (j == 0):
			i += 1
		else:
			j = next[j]
	if (pLen == j):
		return i - j
	return -1  # 見つからない */


#テスト用
if __name__ == '__main__':
	text = "ABCABCABABC"
	pattern = "ABCABA"

	print("position(\"", text, "\", \"", pattern, "\") = ", position(text, pattern))
	