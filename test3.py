# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:06:29 2018

@author: lwj
"""

digits = (1,2,3,4,5,6,7,8,9)
for i in digits:
    ii = i *100
    for j in digits:
        if j == i:
            continue
        jj = j * 10
        for k in digits:
            if k == i or k == j:
                continue
            print(ii + jj + k)