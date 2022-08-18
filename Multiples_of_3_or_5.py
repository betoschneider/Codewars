# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 07:38:42 2022

@author: Roberto Schneider
"""

#link do desafio: https://www.codewars.com/kata/514b92a657cdc65150000006/python

def solution(number):
    if number < 0:
        return 0
    mult = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            mult.append(i)
    soma = 0
    for i in mult:
        soma += i
    return soma


if __name__ == '__main__':
    teste = solution(-10)
    print(teste)