from casadi import *

yadaya = 5


test = 1


def fac(n):
  if n==0:
    return 1
  else:
    return n*fac(n-1)
  
print fac(4)
