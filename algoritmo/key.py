#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basico.utils import *
import random

def genOcteto():
    res = ''
    par = 0
    for i in range(7):
        b = random.randint(0, 1)
        res = res + str(b)
        if b == 1:
            par = par + 1
    
    if par % 2 == 0:
        res = res + '1'
    else:
        res = res + '0'
    
    return res

def genKey():
    res = ''
    for i in range(8):
        res = res + genOcteto()
    return res

def hexKey(key):
    return bytesToHex(key)

def binKey(hexKey):
    return hexToBytes(hexKey)

def checkKey(hexKey):
    
    key = binKey(hexKey)
    
    res = len(key) == 64
    
    if res:
        i = 0
        c = 0
        
        for bit in key:
            
            if (i+1) % 8 == 0:
                
                if (c % 2 == 0 and bit == '0') or (c % 2 == 1 and bit == '1'):
                    res = False
                    break
                
                c = 0
            else:
                if bit == '1':
                    c = c+1
            i = i +1
    
    return res
