#!/usr/bin/env python3 

from sys import path
path.append('../packages/extrapack.zip')

# When using subpackages in Python, it is necessary to specify the full 
# import path for the Python interpreter to correctly 
# find the modules and their functions.
#

from extra.iota import FunI
print(FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
