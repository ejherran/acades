#!/usr/bin/env python
# -*- coding: utf-8 -*-

def intToBin(i):
    b = bin(i).split('b')[1]
    if len(b) < 8:
        b = '0'*(8-len(b))+b
    return b
    
def intToHex(i):
    h = hex(i).split('x')[1].upper()
    if len(h) < 2:
        h = '0'+h
    return h

def intToChar(i):
    return chr(i)

def binToInt(b):
    return int(b, 2)

def binToHex(b):
    return intToHex(binToInt(b))

def binToChar(b):
    return intToChar(binToInt(b))

def hexToInt(h):
    return int(h, 16)

def hexToBin(h):
    return intToBin(hexToInt(h))

def hexToChar(h):
    return intToChar(hexToInt(h))

def charToInt(c):
    return ord(c)

def charToBin(c):
    return intToBin(charToInt(c))

def charToHex(c):
    return intToHex(charToInt(c))
