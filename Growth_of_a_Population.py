# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 07:38:42 2022

@author: Roberto Schneider
"""

#link do desafio: https://www.codewars.com/kata/563b662a59afc2b5120000c6/solutions/python

def nb_year(p0, percent, aug, p):
    # your code
    year = 0
    while p0 < p:
        p0 = int(p0 * (1 + percent / 100) + aug)
        year += 1
    return year


if __name__ == '__main__':
    teste = nb_year(1000, 2, 50, 1363)
    print(teste)