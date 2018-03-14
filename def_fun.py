#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
            raise TypeError('bad operand type')
    elif not isinstance(b,(int,float)):
            raise TypeError('bad operand type')
    elif not isinstance(c,(int,float)):
            raise TypeError('bad operand type')
    elif (b*b-4*a*c)<0:
        raise TypeError('no result')
    else:
        x=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        y=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return (x,y)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
