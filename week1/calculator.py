#!/usr/bin/env python3
import sys
try:
	gongzi = int(sys.argv[1])
	yj = gongzi - 3500
	if yj > 0:
		if yj < 1500:
			s = yj * 0.03
		elif yj < 4500:
			s = yj*0.1 - 105
		elif yj < 9000:
			s = yj*0.2 - 555
		elif yj < 35000:
			s = yj*0.25 - 1005
		elif yj < 55000:
			s = yj*0.3 - 2755
		elif yj <80000:
			s = yj*0.35 - 5505
		else:
			s = yj*0.45 - 13505
	else:
		s = 0
	print("{:.2f}".format(s))
except:
	print("Paramenter Error")


 
	
