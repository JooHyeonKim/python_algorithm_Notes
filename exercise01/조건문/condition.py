x = 15

if x >= 10:
    print('x >= 10')
if x>= 0:
    print('x >= 0')

if x>= 30:
    print('x >= 30')

# 파이썬에서는 코드의 블록을 들여쓰기로 지정합니다.

score = 89
if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')

a = -11

if a>=0:
    print('a>=0')
elif a >= -10:
    print('0 > a >= -10')
else:
    print('-10 > a')

if True or False:
    print('Yes')
if True and False:
    print('yes')

a = 9
if a <= 20 and a >=0:
    print('true')

#in 연산자와 not in 연산자
# 리스트, 튜플, 문자열, 딕셔너리 모두 샤용 가능
# x in 리스트 : 리스트 안에 x가 들어가 있을 때 참
# x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 참

# 파이썬의 pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
# 디버깅 과정에서 일단 조건문의 형태만 만들어놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우

score = 85
if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')
print('프로그램을 종료합니다.')


#코드스타일1
x = 15
if x>0 and x<20:
    print('x는 0 이상 20 미만의 수입니다.')

#코드스타일2
if 0<x<20:
    print('x는 0 이상 20 미만의 수입니다.')

#1부터 9까지 모든 정수의 합 구하기 예제(while문)
i=1
result=0
while i<=9:
    result += i
    i += 1
print(result)

#for문
# for 변수 in 리스트:
#   실행할 소스코드

array = [9,8,7,6,5]
for x in array:
    print(x, end=" ")

result = 0
print()
# i는 1부터 9까지의 모든 값을 순회
for i in range(1,10):
    result += i
print(result)


#continue
#반복문에서 남은 코드의 실행을 건너뛰고 다음 반복을 진행하고자 할 때 continue를 사용합니다.
# 1부터 9까지의 홀수의 합을 구할 때
result = 0
for i in range(1,10):
    if i%2 == 0:
        continue
    result += i

print('1부터 9까지의 홀수의 합 > ',result)

#break
#반복문 즉시 탈출
#1부터 5까지의 정수를 차례대로 출력

i = 1
while True:
    print('i > ',i)
    if i == 5:
        break;
    i+=1


#예제1. 점수가 80점 넘으면 합격
scores = [90,85,77,65,97]