# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:21:05 2022

@author: Roberto Schneider
"""
#link do desafio: https://www.codewars.com/kata/526571aae218b8ee490006f4

#solução do desafio
def count_bits(n):
    b = 0
    while n >= 2:
        b += n % 2
        n = n // 2
    b += n
    return b
print(count_bits(1234))


#converte um inteiro da base 10 para binário
def convert_bin(n):
    b = ''
    while n >= 2:
        b += str(n % 2)
        n = n // 2
    b += str(n)
    return b[::-1]
print(convert_bin(13))