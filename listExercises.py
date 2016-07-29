# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:58:01 2016

@author: Matt
"""
list = ['matt', 'luke', 'jake']
list2 = ['john', 'shaun']
a = range(100)
i = 0
while i < len(a):
    print a[i]
    i = i + 3

list.append('melissa')
print list

list.insert(1, 'tiff')
print list

list.extend(list2)
print list

print list.index('matt')

list.remove('jake')

list.sort()
print list

list.reverse()
print list

print list.pop(2)
print list

list = []
list.append('a')
list.append('b')
print list

list = ['a', 'b', 'c', 'd']
print list[1:-1]
list[0:2] = 'z'
print list