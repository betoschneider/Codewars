# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:51:55 2022

@author: Roberto Schneider
"""


def spin_words(sentence):
    # Your code goes here
    ecnetnes = ''
    for palavra in sentence.split(' '):
        n = len(palavra)
        if n < 5:
            ecnetnes += palavra
        else:
            for i in range(n):
                ecnetnes += palavra[n - 1 - i]
        ecnetnes += ' '
    return ecnetnes.strip()




