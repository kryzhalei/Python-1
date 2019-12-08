# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:57:38 2019

@author: Kryzha Lei Aguilar
"""

import matplotlib.pyplot as plt

def function(n):
    if n <= 9:
        return (n**2) - 7
    elif n >= 10:
        return function(n-10)

x = []
y = []

for character in range(0,100):
    x.append(character)
    y.append(function(character))
    
plt.stem(x,y, use_line_collection = True)    
plt.title('Graph of f(n)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')