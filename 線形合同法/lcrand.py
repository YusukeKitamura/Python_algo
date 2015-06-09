# coding=utf-8
#	lcrand.py -- üŒ`‡“¯–@
#	http://ja.wikipedia.org/wiki/%E7%B7%9A%E5%BD%A2%E5%90%88%E5%90%8C%E6%B3%95

seed = 1
RAND_MAX = 0xffffffff

def init_rnd(x):
	global seed
	seed = x

def irnd():
	global seed
	seed = (seed * 1566083941 + 1) & RAND_MAX
	return seed

def rnd():  # 0 <= rnd() < 1
	val = (1.0 / (RAND_MAX + 1.0)) * irnd()
	return val

init_rnd(12345)  #”CˆÓ‚Ì unsigned long ‚Å‰Šú‰»

for n in range(160):
	data = rnd()
	if n % 10 == 9:
		print('%.6f' % data)
	else:
		print('%.6f' % data, " ", end="")
	