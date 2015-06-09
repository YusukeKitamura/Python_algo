# coding=utf-8
#	roundoff.py -- �l�̌ܓ�
#	a/b��������R�ʂŎl�̌ܓ�

# 0 <= a <= b, b != 0
def round1000(a, b):
	if (a <= 4294967295 / 2000) :
		d = (int)(a * 2000 / b)
	else:
		bl = b % 2000
		bh = (int)(b / 2000)
		d = (int)(a / bh)
		rp = (a % bh) * 2000
		rm = bl * d
		if (rp < rm):
			d -= 1
			rm -= rp
			while (rm > b):
				d -= 1
				rm -= b
	return (int)((d + 1) / 2)

#�e�X�g�p
if __name__ == '__main__':
	print("a = ")
	a = int(input())
	print("b = ")
	b = int(input())
	r = round1000(a, b);
	print("a / b = ", r / 1000, r % 1000)
	