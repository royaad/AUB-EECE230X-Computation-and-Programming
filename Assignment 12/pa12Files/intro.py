# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:09:55 2018

@author: louay
"""


from graph import buildGraphFromFile 
import matplotlib.pyplot as plt
cwd = "c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/"
G = buildGraphFromFile(cwd+"DiGraph1.txt", undirected = False)
print(G)
print(type(G))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G = buildGraphFromFile(cwd+"UndirectedGraph1.txt", undirected = True)
print(G)
plt.figure(2)
plt.clf()
G.draw()
plt.show()