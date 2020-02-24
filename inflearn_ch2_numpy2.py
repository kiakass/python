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
'''
#Indexing & slicing
리스트와 달리 행과 열을 나누어 slicing 이 가능하다.
Matrix의 부분 집합을 추출할 때 유용함
slideshare.net/PyData/introduction-to-numpy
'''
a = np.array([[1,2,3,4,5],[6,7,8,9,10]],int)
a[:,2:]
a[1,1:3]
a[1:3]
a[1]
a[0]

a = np.array([[1,2,5,8],[1,2,5,8],[1,2,5,8],[1,2,5,8]],int)
a[1,:2]
a[:,1:3]

a = np.arange(100).reshape(10,10)
a[:,-1].reshape(-1,1)


'''
#Create function
'''
np.arange(30)
list(range(10))
np.arange(0,5,1)

np.arange(30).reshape(5,6)

np.arange(0,5,0.1)
list(range(0,5,0.1))
np.arange(0,5,0.1).tolist()

#초기화
np.zeros(shape=(10,), dtype=np.int8)
np.zeros((2,5))
np.ones(shape=(10,), dtype=np.int8)
np.ones((2,5))
#초기화시키지않고 비워만줌
np.empty(shape=(10,), dtype=np.int8)
np.empty((3,5))

np.ones((5,6))
test_matrix = np.arange(30).reshape(5,6)
# 1로 값을 채워줌
np.ones_like(test_matrix)

#identity - 단위 행렬을 생성함
np.identity(n=3, dtype=np.int8)
np.identity(n=5)

#eye - 대각선이 1인행렬, k값의 시작 index의 변경
np.eye(N=3, M=5, dtype=np.int8)
np.eye(N=5)
# k = start index
np.eye(N=5,k=2)
np.eye(3,5,k=2 )

#diag - 대각 행렬의 값을 추출함
matrix = np.arange(9).reshape(3,3)
np.diag(matrix)
np.diag(matrix,k=1)

#random sampling - 데이터 분포에 따른 sampling
#uniform : 균등분포
np.random.uniform(0,1,10).reshape(2,5)
#normal : 정규분포 표준편차 1: 1시그마내 1.96
np.random.normal(0,2,10).reshape(2,5)
