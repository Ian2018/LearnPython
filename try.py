#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t1 = (1,2,3)
t2 = (1,[2,3])

try:
    d1 = {t1:t2}
    print('d1=',d1)
    d2 = {t2:t1}
    print('d2=',d2)
except TypeError as e:
    print('error:%s\n'%e)

try:
    s = {t1}
    print('s=',s)
except TypeError as e:
    print('error:',e)
