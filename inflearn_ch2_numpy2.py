# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:30:24 2020

# Numerial python - numpy : Data handling 
# Matrix 와 Vector 와 같은 Array 연산의 사실상의 표준

# Numpy 특징
- 일반 List에 비해 빠르고 메모리 효율적
- 반복문 없이 데이터 배열에 대한 처리를 지원함
- 선형대수와 관련된 다양한 기능을 제공함
- C, C++, 포트란등의 언어와 통합 가능

# ndarray : numpy dimensional array
- 하나의 데이터 type 만 배열에 넣을 수 있음
- C를 array 를 사용하여 배열을 생성함
"""
import numpy as np

test_array = np.array(["1",4,5,8],np.int32)
test_array
type(test_array[3])
test_array.dtype
test_array.shape

matrix = [[1,2,5,8,],[1,2,5,8],[1,2,5,8]]
matrix.shape
np.array(matrix).shape
np.array(matrix).flatten()

matrix = np.array([[1,2,5,8,],[1,2,5,8],[1,2,5,8]])
matrix.shape
matrix.size
matrix.ndim
# size 가 같으면 reshape 이 가능함
matrix.reshape(2,2,3)
matrix.reshape(1,1,2,6)
matrix.flatten()
