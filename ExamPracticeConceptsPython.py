class tp:
    def __init__(self,real,imag):
        self.real=real
        self.__imag=imag
    def tp_fun(self):
        print(self.__imag)

c = tp(2,3)
c.tp_fun()
li = [1,2,3,4,1,2,3,4,5,6,3,1]
print(li.remove(1))
print(li.remove(1))
print(li.remove(1))

print(li.count(1))

import time
print(time.asctime(time.localtime(time.time())))

import calendar
print(calendar.month(2017,11))


import datetime
print(datetime.MAXYEAR,datetime.MINYEAR)

import numpy as np
import os
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1
if __name__=="__main__":
    print (Money)
    AddMoney()
    print (Money)
    print(locals())
    print(globals())
    print(os.getcwd())
    a=np.array([1,2,3,4],int)
    print(a)
    a.fill(0)
    print(a)