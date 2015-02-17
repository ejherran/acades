#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numbers import *

def stringToBytes(s):
    res = ''
    for c in s:
        res = res + charToBin(c)
    return res

def bytesToString(b):
    res = ''
    z = len(b)/8
    c = 0
    while(c < z):
        res = res + binToChar( b[(8*c):(8*(c+1))] )
        c = c + 1
    return res
    
def stringToHex(s):
    res = ''
    for c in s:
        res = res + charToHex(c)
    return res

def hexToString(h):
    res = ''
    z = len(h)/2
    c = 0
    while(c < z):
        res = res + hexToChar( h[(2*c):(2*(c+1))] )
        c = c + 1
    return res

def bytesToHex(b):
    res = ''
    z = len(b)/8
    c = 0
    while(c < z):
        res = res + binToHex( b[(8*c):(8*(c+1))] )
        c = c + 1
    return res

def hexToBytes(h):
    res = ''
    z = len(h)/2
    c = 0
    while(c < z):
        res = res + hexToBin( h[(2*c):(2*(c+1))] )
        c = c + 1
    return res

def permuta(tab, data):
    res = ''
    for i in tab:
        res = res + data[i-1]
    return res

def rotLeft(s, n):
    a = s[0:n]
    s = s + a
    return s[n:]

def rotRight(s, n):
    l = len(s)
    a = s[l-n:]
    s = a + s
    return s[0:l]

def XOR(a, b):
    
    res = ''
    
    for i in range(len(a)):
        if a[i] == '0' and b[i] == '0':
            res = res+'0'
        elif a[i] == '0' and b[i] == '1':
            res = res+'1'
        elif a[i] == '1' and b[i] == '0':
            res = res+'1'
        elif a[i] == '1' and b[i] == '1':
            res = res+'0'
    
    return res

def unBox(s, i, j):
    return s[i][j]
