#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product(x,*numbers):
    for n in numbers:
        x=x*n
    return x



#test
print('product(5) = ',product(5))
print('product(5,6) = ',product(5,6))
print('product(5,6,7) = ',product(5,6,7))
print('product(5,6,7,9) = ',product(5,6,7,9))
if product(5) != 5:
    print('test defeade!')
elif product(5,6) != 30:
    print('test defeade!')
elif product(5,6,7) != 210:
    print('test defeade!')
elif product(5,6,7,9) != 1890:
    print('test defeade!')
else:
    try:
        product()
        print('test defeade!')
    except TypeError:
        print('test success!')
