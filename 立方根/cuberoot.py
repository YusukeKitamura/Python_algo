# coding=utf-8
#	cuberoot.py -- 立方根

def cuberoot(x):  # \sqrt[3]{x}
	if x == 0:
		return 0.0
	if x > 0:
		positive = 1
	else: 
		positive = 0
		x = -x
	if x > 1:
		s = x
	else:
		s = 1.0
	
	prev = s + 1.0
	while s < prev:
		prev = s
		s = (x / (s * s) + 2.0 * s) / 3.0

	if positive == 1:
		return prev
	else:
		return -prev

def cuberoot2(x):  #\sqrt[3]{x}
	if x == 0:
		return 0.0
	if x > 0:
		positive = 1
	else: 
		positive = 0
		x = -x
	if x > 1:
		s = x
	else:
		s = 1.0
	
	prev = s + 1.0
	while s < prev:
		prev = s
		t = s * s
		s += (x - t * s) / (2 * t + x / s)

	if positive == 1:
		return prev
	else:
		return -prev

def lcuberoot(x):
	if x == 0:
		return 0.0
	s = cuberoot(x)
	return (x / (s * s) + 2.0 * s) / 3.0

#テスト用
if __name__ == '__main__':
for i in range(0, 20):
	print(i, " ", cuberoot(i), " ", cuberoot(i))

