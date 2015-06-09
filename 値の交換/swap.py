# coding=utf-8
# swap.py -- ’l‚ÌŒðŠ·

def swap(x, y):
	temp = x
	x = y
	y = temp

#def swap1(x, y):
#	*y ^= *x
#	*x ^= *y
#	*y ^= *x

#def swap2(x, y)
#	*y = *x - *y
#	*x -= *y
#	*y += *x

print("x:")
x = int(input())

print("y:")
y = int(input())

print("x = ", x, "y = ", y)
swap(x, y)
print("x = ", x, "y = ", y)
