#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#def triangaes():
#    a=[1]
#    yield a[:]
#    a += [1]
#    yield a[:]
#    for x in range(3,15):
#        a.insert(x//2,(a[x//2-1] +a[x//2]))
#        if x%2 == 0:
#            a[(x//2)-1]=a[x//2]
#        if (x-2-x//2)>0:
#            for n in range(1,x-x//2-1):
#                a[x//2+n]=a[x//2+n]+a[x//2+n+1]
#                a[-(x//2+n+1)]=a[-(x//2+n+1)]+a[-(x//2+n+2)]
#        yield a[:]

def triangaes():
    a=[1]
    while 1 :
        yield a
        a=a+[0]
        a=[a[i]+a[i-1] for i in range(len(a))]


#def triangaes():
#    a = [1]
#    while 1:
#        yield a
#        a = [1] + [ a[n] + a[n+1] for n in range(len(a)-1) ]  + [1] 

#print(triangaes())

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
resuats = []
for t in triangaes():
    print(t)
    resuats.append(t)
    n = n + 1
    if n == 10:
        break

print('\n')
print(resuats)

if resuats == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
