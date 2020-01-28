# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:24:03 2020

@author: junhk
"""
import pandas as pd
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
df_data = pd.read_csv(data_url, sep='\s+', header=None)
df_data.head()

df_data.columns = ['CRIM', 'ZN',  'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df_data.head(10)

import numpy as np

# column 형식의 값을 넣기 위해 2차원 배열을 사용함
weight_vector = np.array([[1],[1], [1]])
x_vector = np.array([[3], [4], [5]])

weight_vector.T.dot(x_vector)
df_data.values[0]
df_data.as_matrix()

df_data['weight_0'] = 1
df_data.head

df_data = df_data.drop("MEDV", axis=1)

df_data.shape()

df_matrix = df_data.as_matrix()
weight_vector = np.random.random_sample((14,1))
weight_vector

(df_matrix.dot(weight_vector)).shape
