# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 07:38:42 2022

@author: Roberto Schneider
"""

#link do desafio: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    #your code here
    diff = []
    for i in a:
        if i not in b:
            diff.append(i)
    return diff


if __name__ == '__main__':
    teste = array_diff([1,2,2,2,3],[2])
    print(teste)