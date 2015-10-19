from casadi import *

yadaya = 2


test = 1


def fac(n):
  p = 1


  while n>0:
   p*= n
   n = n -1
  return p
  
print fac(4)
