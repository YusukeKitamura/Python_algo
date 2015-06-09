# coding=utf-8
#	neville.py -- Neville (ネヴィル) 補間
from decimal import *
getcontext().prec = 8

def neville(t, x, y, N):
	w = [0.0] * N	#初期化

	for i in range(N):
		w[i] = y[i]
		for j in range(i-1, -1, -1):
			w[j] = w[j + 1] + (w[j + 1] - w[j]) * (t - x[i]) / (x[i] - x[j])
			
	return round(w[0], 6)

#  Aitken (エイトケン) 補間
def aitken(t, x, y, N):
	w = [0.0] * N	#初期化

	for i in range(N):
		w[i] = y[i]
	
	for j in range(1, N):
		for k in range(N-1, j-1, -1):
			w[k] = (w[k-1]*(x[k]-t) - w[k]*(x[k-j]-t)) / (x[k]-x[k-j])
			
	return round(w[N - 1], 6)


x = [0.0, 10.0, 20.0, 30.0, 40.0]
y = [610.66, 1227.4, 2338.1, 4244.9, 7381.2]	# データ
N = 5		# データの数

print("Neville")
for i in range(10, 31):
	print(i, " ", neville(i, x, y, N))
	
print("Aitken")
for j in range(10, 31):
	print(j, " ", aitken(j, x, y, N))
