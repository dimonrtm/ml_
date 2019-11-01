# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:10:30 2019

@author: dim
"""

import sympy as sy
import numpy as np
from Newton import Newton
formula=input("Введите формулу:")
x=float(input("Введите начальный  x:"))
y=float(input("Введите начальный y:"))
opt=Newton(formula,x,y)
opt_x=opt.newton()
print("Оптимальный x:")
print(opt_x)