from casadi import *

yadaya = 2


test = 1


def fac(n):
  return n*fac(n-1)
  
print fac(4)
