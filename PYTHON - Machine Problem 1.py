# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:17:48 2019

@author: Kryzha Lei Aguilar
"""

import matplotlib.pyplot as plt
import numpy as np

def problem1(n):
    if (n>=0) and (n<=9):
        return (n**2) - 7
    elif n >= 10:
        return problem1(n-10)
    else:
        return;

x = np.arange(100)
y = []
for num in x:
    y.append(problem1(num))

plt.stem(x,y, use_line_collection = True)    
plt.show()