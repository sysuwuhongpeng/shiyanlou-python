#!/usr/bin/env python3
import sys

gongziList = {}
try:
    for arg in sys.argv[1:]:
        lists = arg.split(':')
        gonghao = int(lists[0])
        gongzi  = int(lists[1])
        yj = gongzi - gongzi*0.165 - 3500
        if yj > 0:
            if yj <= 1500:
                s = yj * 0.03
            elif yj <= 4500:
                s = yj*0.1 - 105
            elif yj <= 9000:
                s = yj*0.2 - 555
            elif yj <= 35000:
                s = yj*0.25 - 1005
            elif yj <= 55000:
                s = yj*0.3 - 2755
            elif yj <= 80000:
                s = yj*0.35 - 5505
            else:
                s = yj*0.45 - 13505
        else:
            s = 0
        gongzi -= (s + gongzi*0.165) 
#        print("{}:{:.2f}".format(gonghao,s))
        gongziList[gonghao] = gongzi
    for key,value in gongziList.items():
        print("{}:{:.2f}".format(key,value))
except:
    print("Paramenter Error")



 
	
