# coding=utf-8
#	105.py -- 百五減算

def hyakugo(a, b, c):
	return (70 * a + 21 * b + 15 * c) % 105

print("1から100までの整数を1つ考えてください")

print("それを 3 で割った余り?")
a = int(input())

print("それを 5 で割った余り?")
b = int(input())

print("それを 7 で割った余り?")
c = int(input())

x = hyakugo(a, b, c)
print("あなたの考えた数は", x, "でしょう!")
