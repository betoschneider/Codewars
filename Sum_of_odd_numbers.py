# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:21:18 2022

@author: Roberto Schneider
"""

#link do desafio: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python


def row_sum_odd_numbers(n):
    #your code here
    inicio = sum([x for x in range(n)]) * 2 +1
    fim = inicio + (n - 1) * 2
    return sum([x for x in range(fim + 1)[::-1] if x >= inicio and x % 2 == 1]) 


a = row_sum_odd_numbers(1)
a = row_sum_odd_numbers(2)
a = row_sum_odd_numbers(3)
a = row_sum_odd_numbers(4)
a = row_sum_odd_numbers(5)