# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 07:38:42 2022

@author: Roberto Schneider
"""

#link do desafio: https://www.codewars.com/kata/514b92a657cdc65150000006/python

def solution(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])

if __name__ == '__main__':
    teste = solution(10)
    print(teste)