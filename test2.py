# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:03:12 2018

@author: lwj
"""

for i in range(100, 1000):
    ge=i%10
    shi=i//10%10
    bai=i//100
    if ge**3+shi**3+bai**3==i:
        print(i)
    