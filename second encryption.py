#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:19:49 2019

@author: Sina
"""

import string
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def switcher(char1, char2, str1): #switches all instances of two characters in str1 and returns it as str2
    str2 = ''
    for i, char in enumerate(str1):
        #if (char in alphabets):
        if char == char1:
            str2 += char2
        elif char == char2:
            str2 += char1
        else:
            str2 += char
    return str2

code = "dk. afr dkl. rwklstb, gy fwdztk ygwk, hkoxtm rkoxt, ctkt hkgwr mg lab miam mitb ctkt htkytemsb fgkdas, miafq bgw xtkb dwei. mitb ctkt mit salm htghst bgw’r tvhtem mg zt ofxgsxtr of afbmiofu lmkafut gk dblmtkogwl, zteawlt mitb pwlm rorf’m igsr comi lwei fgfltflt."

alphabets = string.ascii_lowercase
frequency_order = 'etaoinsrhdlucmfywgpbvkxqjz' #found this ranking in internet.

initial_answer = ''


instances_of_letter = np.zeros( len(alphabets) )
for x in alphabets:
    #print(x)
    instances_of_letter[ alphabets.index(x) ] = code.count(x)


for i, char in enumerate(code): #this part swaps the letter based on the frequency of letters in english.
    if (char in alphabets):        
        initial_answer += frequency_order[ list(instances_of_letter.argsort()[::-1]).index( alphabets.index(char)  )]
    else:
        initial_answer += char


#we have already got phrases like "to be"

#the first part seems to be mr. and ms. (courtesy of Moneem which figured this out.)
#manual_answer = switcher('m', 'f', initial_answer)
manual_answer = switcher('a', 'r', initial_answer)
manual_answer = switcher('f', 'm', manual_answer)
manual_answer = switcher('s', 'n', manual_answer)
manual_answer = switcher('a', 'd', manual_answer)
manual_answer = switcher('i', 'n', manual_answer)
manual_answer = switcher('d', 'l', manual_answer)

#op nlmbr polr-> of number four
manual_answer = switcher('f', 'p', manual_answer)
manual_answer = switcher('l', 'u', manual_answer)
#gere -> were
manual_answer = switcher('g', 'w', manual_answer)
#sai & thei -> say & thei
manual_answer = switcher('i', 'y', manual_answer)
#perfeitcy -> perfectly
manual_answer = switcher('i', 'c', manual_answer)
manual_answer = switcher('i', 'l', manual_answer)
#gery much -> very much
manual_answer = switcher('g', 'v', manual_answer)
#eqpect -> expect
manual_answer = switcher('q', 'x', manual_answer)


print(manual_answer)