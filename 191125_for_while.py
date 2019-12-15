# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:59:42 2019

@author: Administrator
"""

money=True
if money:
   print("택시를", end=' ')
   print("타고", end=' ')
   print("가라")
else :
   print("")
   
1 not in [1,2,3]

score=70
if score >= 60:
    message = "success"
    print(message)
else:
    message = "failure"
    print(message)


""" While 문 만들기 """
   
treeHit = 0
while treeHit < 10:
    treeHit += 1
#    print(treeHit)
    print("나무를 %d번 찍었습니다." % treeHit )
    if treeHit == 10:
        print("나무 넘어갑니다.")

prompt = """
 1. Add
 2. Del
 3. List
 4. Quit
 Enter number : """
        
number = 0
while number != 4:
    print(prompt)
    number = int(input())
    
    
""" 커피 10잔을 다 팔면 중지 메시지 """
coffee = 10
while coffee > 0 :
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피량은 %d 잔 입니다." % coffee )
    
    
""" 커피 10잔 팔기, 돈을 입력받고 300보다 크면 거스름돈, 작으면 커피안줌 
10잔 다 팔면 중지 """

coffee = 3
while True:
    money = int(input("돈을넣어주세요: "))
    if coffee > 0 and money == 300:
        coffee -= 1
        print("커피를 줍니다. 커피가 %d 잔 남았습니다." % coffee )
    elif coffee > 0 and money < 300:
        print("돈이 %d 원 모자랍니다." % (300-money))
    elif coffee > 0 and money > 300:
        coffee -= 1
        print("커피를 줍니다. 커피가 %d 잔 남았습니다." % coffee )
        print("거스름돈 %d 를 가져가세요." % (money-300))
    else:
        print("커피가 다 떨어졌습니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

""" 1부터 10까지의 숫자 중에서 홀수만 출력 """
number = 10
while True:
    a = number % 2
    if a != 0 :
        print("홀수만 출력 : %d" % number)
    elif number == 0:
        break
    number -= 1

a=0
while a < 10:
    a += 1
    if a % 2 == 0 : continue #짝수면 조건으로 돌아가고 아니면 아래를 실행
    print(a) 
    
""" 상당히 중요한 개념임 """

# for
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (i,j) in a:
    print("i: %d + j:%d =" % (i,j))
    print(i+j)    


# for
""" 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 
그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."""

marks=[90, 35, 67, 45, 80]
for mark in marks:
    if mark >= 60:
        print(" %d : 합격" % mark)
    else:
        print(" %d : 불합격" % mark)

""" continue : for 문 처음으로 돌아감 """
marks=[90, 35, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print( "%d 번 %d 점으로 합격입니다." % (number,mark))

""" for 문과 함께 사용하는 range 함수 """
marks=[90, 35, 67, 45, 80]
number = 0
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print(" %d 번 학생 %d점으로 합격입니다." % (number+1,marks[number]))

""" for 를 이용한 구구단 """
for i in  range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")  # end:매개변수 -> 행을 붙여라 """
        #print("%d " % (i*j))
    print(' ')

# end 용법 : 행바꾸지 않고 출력하기
print('주문하실 음료를 알려주세요 :',  end= '')
drink = input()

print('카페라테', end=', ')
print('아메리카노', end=', ')
print('비엔나', end='...')

""" 리스트 내포 """
a = [1,2,3,4]
result = [ num*3 for num in a if num % 2 == 0 ]
print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)

a = 'Life is too short, you need python'
if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('oython')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')

# 연습문제
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
b=0
for i in range(1,1000):
    if i % 3 == 0:
        b = b + i
print(b)

a="*"
i=1
while i <= 5:
    b = a * i
    i += 1
    print(b)
 
for i in range(1,101):
    print(i, end=' ')

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
b=0
for i in a:
   b += i
print(b/len(a))

# 리스트내포
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)
        
numbers = [1, 2, 3, 4, 5]        
result = [ num*2 for num in numbers if num % 2 == 1]
print(result)
