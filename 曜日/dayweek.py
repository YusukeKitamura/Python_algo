# coding=utf-8
#	dayweek.py -- —j“ú
import math

def dayweek(year, month, day):
	name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',' Saturday']
	
	# ‚PŒA‚QŒ‚Í‘O”N‚Ì‚P‚RŒA‚P‚SŒ‚Æ‚İ‚È‚·
	if (month < 3) :
		year -= 1
		month += 12
		
	tmp1 = year + math.floor(year / 4) - math.floor(year / 100) + math.floor(year / 400)
	tmp2 = math.floor((13 * month + 8) / 5) + day
	dayofweek = (tmp1 + tmp2) % 7
	return name[dayofweek]

print("Year?")
year = int(input())
if (year < 1) :
	print("Year is  more than 0 !")
	exit()

print("Month?")
month = int(input())
if (month < 1 or month > 12) :
	print("Month is 1 - 12 !")
	exit()

print("Day?")
day = int(input())
if (day < 1 or day > 31) :
	print("Day is 1 - 31 !")
	exit()

print(dayweek(year, month, day))
