# coding=utf-8
#	eulerian.py -- Euler (ƒIƒCƒ‰[) ‚Ì”
#	http://en.wikipedia.org/wiki/Eulerian_number

# n >= 0
def Eulerian(n, k):
	if k == 0 :
		return 1
	if k < 0 or k >= n :
		return 0
	return (k + 1) * Eulerian(n - 1, k) + (n - k) * Eulerian(n - 1, k - 1)

if __name__ == '__main__':
	MaxVal = 9;

	print("  k", end="")
	k = 0
	while k <= MaxVal:
		print(repr(k).rjust(7), end="")
		k += 1
			
	print("")
	print("n  ", end="")

	k = 0
	while k <= MaxVal:
		print("-------", end="")
		k += 1
			
	print("")

	n = 0
	while n <= MaxVal:
		print(n, end="")
		print(" |", end="")
		k = 0
		while k <= n:
			eul = Eulerian(n, k)
			print(repr(eul).rjust(7), end="")
			k += 1
		print("")
		n += 1
	