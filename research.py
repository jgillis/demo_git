from casadi import *

yadaya = 5


test = 3


def fac(n):
  p = 1


  while n>0:
   p*= n
   n = n -1
  return p
  
print fac(4)
