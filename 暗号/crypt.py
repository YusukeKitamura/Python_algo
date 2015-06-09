# coding=utf-8
#	crypt.py -- 暗号
import sys
import random
from ctypes import *
RAND_MAX = 0xffffffff

def crypt(input, output, seed):
	random.seed(seed)

	fin = open(input, 'r')
	fout = open(output, 'w')
	datas = fin.read()

	for i in range(len(datas)):
		data = datas[i]
		r = random.randint(0, 255)
		out = chr((ord(data) ^ r) % 128)
		fout.write(str(out))
		
	fin.close()
	fout.close()


argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数
if (argc < 3):   # 引数が足りない場合は、その旨を表示
    print('Usage: # python crypt infile outfile seed')
    quit()

crypt(argvs[1], argvs[2], argvs[3])