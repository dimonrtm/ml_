# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:33:24 2019

@author: dim"""
import sympy as sy
import numpy as np

class Newton:
    def __init__(self,formula,x_0,y_0,eps=0.000001):
        self._formula=formula
        self._x_0=x_0
        self._y_0=y_0
        self._eps=eps
        
    def newton(self):
        sy_formula=sy.sympify(self._formula)
        x,y=sy.symbols("x y")
        fx=sy_formula.diff(x)
        fy=sy_formula.diff(y)
        fxx=fx.diff(x)
        fxy=fx.diff(y)
        fyx=fy.diff(x)
        fyy=fy.diff(y)
        x_step=np.array([self._x_0,self._y_0])
        i=0
        while True:
            print("Step "+str(i))
            grad=np.array([float(fx.evalf(subs={x:x_step[0],y:x_step[1]})),float(fy.evalf(subs={x:x_step[0],y:x_step[1]}))])
            hessian=np.array([[float(fxx.evalf(subs={x:x_step[0],y:x_step[1]})),float(fxy.evalf(subs={x:x_step[0],y:x_step[1]}))],
                              [float(fyx.evalf(subs={x:x_step[0],y:x_step[1]})),float(fyy.evalf(subs={x:x_step[0],y:x_step[1]}))]])
            inverse=np.linalg.inv(hessian)
            delta=-inverse.dot(grad)
            lambda_square=grad.T.dot(inverse).dot(grad)
            if (lambda_square/2)<=self._eps:
                break
            alpha=0.1
            beta=0.7
            t=1
            while float(sy_formula.evalf(subs={x:x_step[0]+t*delta[0],y:x_step[1]+t*delta[1]}))>float(sy_formula.evalf(subs={x:x_step[0],y:x_step[1]}))+alpha*t*grad.T.dot(delta):
                t=beta*t
            x_step=x_step+t*delta
            print("X для следующего шага:")
            print(x_step)
            i=i+1
        return x_step