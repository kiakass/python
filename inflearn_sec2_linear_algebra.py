# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:12:34 2020

matrix의 이해
"""
import numpy as np



u = [1,2,3]
v = [4,4,4]
u + v
2*[2*sum(t) for t in zip(u,v)]
[t for t in zip(u,v)]

# Matrix representation of python

matrix_a = [[3, 6], [4, 5]] #List
matrix_b = [(3, 6), (4, 5)] # Tuple
matrix_c = {(0,0): 3, (0, 1): 6, (1, 0):4, (1, 1): 5} #dict

print(matrix_a)
matrix_b
matrix_c

# matrix 합
a= [[3, 6], [5, 8]]
b= [[4, 5], [6, 7]]
[t for t in zip(a,b)]
[[row for row in zip(*t)] for t in zip(a,b)]
[[sum(row) for row in zip(*t)] for t in zip(a,b)]

# np array 활용
a= np.array([[3, 6], [5, 8]])
b= np.array([[4, 5], [6, 7]])
a+b

#scalar matrix product
matrix_a = [[3, 6], [4, 5]]
alpha = 4
[t for t in matrix_a]
[[alpha * element for element in t ] for t in matrix_a]

#matrix transpose
matrix_a = [[1, 2, 3], [4, 5, 6]]
[t for t in zip(*matrix_a)]
[[element for element in t] for t in zip(*matrix_a)]

np.array([[1, 2, 3], [4, 5, 6]]).reshape(3,2)

#matrix product
