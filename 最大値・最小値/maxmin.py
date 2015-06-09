# coding=utf-8
#	maxmin.py -- Å‘å’lEÅ¬’l

def max2(x, y):
	if x > y:
		return x
	else:
		return y
		
def min2(x, y):
	if x < y:
		return x
	else:
		return y

def findmax(a):
	max = a[0]
	for i in range(len(a)):
		if a[i] > max:
			max = a[i]

	return max

def findmin(a):
	min = a[0]
	for i in range(len(a)):
		if a[i] < min:
			min = a[i]

	return min

def findmaxmin(a):
	max = a[0]
	min = a[0]
	for i in range(len(a)):
		if a[i] > max:
			max = a[i]
		elif a[i] < min:
			min = a[i]
	
	return [max, min]


a = [ 3, 1, 33, 10]
pmax = 0
pmin = 0

print("max2(1, 7):")
print(max2(1,7))
print("min2(1, 7):")
print(min2(1,7))

print("a[] = [ 3, 1, 33, 10]")
print("findmax(a)")
print(findmax(a))
print("findmin(a)")
print(findmin(a))
print("findmaxmin(a)")
maxandmin = findmaxmin(a)
print("max=", maxandmin[0])
print("min=", maxandmin[1])
