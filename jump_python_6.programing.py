# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:15:42 2019

@author: Administrator
"""

for i in range(2,10):
    print(" ")
    for j in range(1,10):
        print(i*j, end=" ")
        
        
def GuGu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result

print(GuGu(int(input())))

def GuGu(n):
    i = 0
    result = []
    while i < 10:
        i += 1
        result.append(n*i)
    return result
print(GuGu(int(input())))

'''
10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
'''
import time

def Addmul(o,p):
    i,j,k = 1,0,0
    while i < 1000:
        if i % o == 0 or i % p == 0:
            j += i
#            time.sleep(1)
        i += 1
        print("i,j,k %d %d" % (i,j))
    return j

print(Addmul(3,5))

result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)

'''
06-3 게시판 페이징하기
A 씨는 게시판 프로그램을 작성하고 있다. 그런데 게시물의 총 건수와 한 페이지에 
보여 줄 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.

구조화
1. function name : GetPageNo
2. input : m(게시물의 총건수), n(한페이지 게시물의 수)
3. output : o(총페이지수)
'''
o,p = 0,0
def GetPageNo(m, n):
    o = m // n
    p = m % n
    if p > 0:
        o = o + 1
    return o

print(GetPageNo(35,4))

def GetPageNo(m, n):
    if m // n == 0:
        return m // n
    else:
        return m // n + 1

print(GetPageNo(35,4))

'''
06-4 메모장 만들기
메모를 파일엥 저장하고 추가 및 조회가 가능한 간단한 메모장
'''



