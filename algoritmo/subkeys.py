#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basico.utils import *

PC_1 =        [57, 49, 41, 33, 25, 17,  9]
PC_1 = PC_1 + [ 1, 58, 50, 42, 34, 26, 18]
PC_1 = PC_1 + [10,  2, 59, 51, 43, 35, 27]
PC_1 = PC_1 + [19, 11,  3, 60, 52, 44, 36]
PC_1 = PC_1 + [63, 55, 47, 39, 31, 23, 15]
PC_1 = PC_1 + [ 7, 62, 54, 46, 38, 30, 22]
PC_1 = PC_1 + [14,  6, 61, 53, 45, 37, 29]
PC_1 = PC_1 + [21, 13,  5, 28, 20, 12,  4]

PC_2 =        [14, 17, 11, 24,  1,  5]
PC_2 = PC_2 + [ 3, 28, 15,  6, 21, 10]
PC_2 = PC_2 + [23, 19, 12,  4, 26,  8]
PC_2 = PC_2 + [16,  7, 27, 20, 13,  2]
PC_2 = PC_2 + [41, 52, 31, 37, 47, 55]
PC_2 = PC_2 + [30, 40, 51, 45, 33, 48]
PC_2 = PC_2 + [44, 49, 39, 56, 34, 53]
PC_2 = PC_2 + [46, 42, 50, 36, 29, 32]

KEY_ROT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def getSubKeys(key):
    
    kp = permuta(PC_1, key)
    
    C0 = kp[0:28]
    D0 = kp[28:56]
    
    CN = [C0]
    DN = [D0]
    
    i = 0
    while(i < len(KEY_ROT)):
        CN.append( rotLeft(CN[i], KEY_ROT[i]) )
        DN.append( rotLeft(DN[i], KEY_ROT[i]) )
        i = i + 1

    KN = ['000000000000000000000000000000000000000000000000']
    
    for i in range(1, 17):
        KN.append( permuta(PC_2, CN[i]+DN[i]) )

    return KN
