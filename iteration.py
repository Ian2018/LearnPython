#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#def findMinAndMax(L):
#    if len(L)!=0:
#        maxl=L[0]
#        minl=L[0]
#    else:
#        maxl=None
#        minl=None
#
#    for n in L:
#        if maxl < n:
#            maxl = n
#        if minl > n:
#            minl = n
#
#    return (minl,maxl)

def findMinAndMax(L):
    if len(L) == 0:
        return None,None
    for n in [L]:
        return min(n),max(n)

    print('%s!',findMinAndMax([]))
    print('%s!',findMinAndMax([7]))
    print('%s!',findMinAndMax([7,1]))
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
