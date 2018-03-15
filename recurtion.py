#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#def fact(n):
#    if n==1:
#        return 1
#    return n * fact(n-1)


def fact(n):
    return fact_iter(n,1)

def fact_iter(n,product):
    if n==1:
        return product
    return fact_iter(n-1,n*product)


#def fact(n):
#    sumnub=n
#    while n >1:
#        n=n-1
#        sumnub=sumnub*(n)
#    return sumnub

