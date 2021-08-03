#!/usr/bin/python3
import sys
argvs = sys.argv
argc = len( argvs )
months=[31,28,31,30,31,30,31,31,30,31,30,31]
youbia = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def dayofweek(year, month, day):
  m = (month-3)%12
  y = year if month >= 3 else year - 1
  n = day + (13*m+2)//5 + y + y//4 - (y//100) + y//400 + 2
  return (n%7)

def printcal(y,m):
  mm=months[m-1]+(1 if (m==2 and (y%4 == 0 and y%100 != 0 or y%400 == 0)) else 0)
  print(y,m,sep='/')
  print (*youbia,sep=' ')
  f=dayofweek(y,m,1)
  print("    "*f,end='')
  for i in range(1,mm+1):
    print(" %2d " %i,end='')
    if f==6:
      print("")
    f=(f+1)%7
  if f!=0:
    print("")

if argc==3:
  y = int(sys.argv[1])
  m = int(sys.argv[2])
  printcal(y,m)
elif argc==4:
  y = int(sys.argv[1])
  m = int(sys.argv[2])
  d = int(sys.argv[3])
  f = dayofweek(y,m,d)
  print(y, "/", m, "/", d, " is ", youbia[f],sep="")

else:
  print("Usage : cal.py y m [d]")
  exit(1)
