a = [1,2,3,4,5,6,7,8,9]

print(a[3])
#리스트 컴프리헨션
#a[1]부터 a[3]까지 출력
print(a[1:4])

#0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 == 1]
print(array)

#1부터 9까지의 수들의 제곱을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

#리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용됨.
# N X M 크기의 2차원 리스트를 한 번에 초기화할 때 유용
N = 2
M = 3
array = [[0]*M for _ in range(N)]
print(array)


#파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용합니다.

for _ in range(5):
    print("Hello World")

array = [i for i in range(10)]
print(array)
array.append(100)
print(array)

array.sort(reverse=True)
print(array)

array.reverse()
print(array)

array.insert(1,1.5)
print(array)
array.append(1)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5} #집합 자료형

#remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

data = "Don't you know \"Python?\""
print(data)

#문자열 연산

a = 'Hello'
b = 'World'
print(a+ " "+b)

a = 'String'
print(a*3)

a = 'ABCDEF'
print(a[2 : 4])

# a[2] = 'Z' -> 실행오류
#문자열 객체는 원소삽입을 지원하지 않

#튜플 자료형
#튜플은 리스트와 유사하지만 다음과 같은 문법적 차이가 있습니다.
#   튜플은 한 번 선언된 값을 변경할 수 없습니다.
#   리스트는 대괄호 []를 사용하지만 튜플은 소괄호 ()를 사용합니다.
#튜플은 리스트에 비해 상대적으로 기능이 제한적이기 때문에 공간 효율적입니다.

tuple = (1,2,3,4,5,6,7,8,9)

#네 번째 원소만 출력
print(tuple[3])

#두 번째 원소부터 네 번째 원소까지
print(tuple[1:4])

#튜플은 변경이 불가능한 객체
# tuple[5]=10  실행오류

#튜플을 사용하면 좋은 경우
#- 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
#   최단 경로 알고리즘에서는 (비용, 노드번호)의 형태로 튜플 자료형을 주로 사용합니다.
#데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
#   튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있습니다.
#리스트보다 메모리를 효율적으로 사용해야 할 때


#6.사전, 집합 자료형

#사전 자료형
#-사전 자료형은 key와 value의 쌍을 데이터로 가지는 자료형입니다.
#   앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됩니다.
#사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 불가능한(immutable) 자료형'을 키로 사용할 수 있습니다.
# 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

#키 데이터만 담은 리스트
key_list = data.keys()

#값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {
    '홍길동' : 97,
    '이순신' : 98
}

print(b)
key_list = b.keys()
value_list = b.values()
print(key_list)
print(value_list)

print(b['이순신'])

#집합 자료형
#집합의 특징 - 중복을 허용하지 않는다. - 순서가 없다.
#집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있습니다.
#   이 때 set()함수를 이용합니다.
# 혹은 중괄호 ({}) 안에 각 원소를 콤마를 기준으로 구분하여 삽임함으로써 초기화할 수 있습니다.
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.(사전자료형과 동일)


#집합 자료형 초기화 방법 1
data = set([1,1,2,3,4,4,5])
#중복되는 원소들은 제거됨.
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

#집합자료형의 연산
#기본적인 집합 연산으로는 합집합, 교집합, 차집합 연산 등이 있습니다.

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

#합집합
print(a|b)

#교집합
print(a&b)

#차집합
print(a-b)

data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#새로운 원소 여러 개 추가
data.update([5,6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

#사전 자료형과 집합 자료형의 특징
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.
# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
#   사전의 key 혹은 집합의 원소(element)를 이용해 O(1)의 시갖 복잡도로 조회합니다.


#기본 입출력
#예. 학생의 성적이 주어지고, 이를 내림차순으로 정렬한 결과를 출력
#입력예시
#5
#65 90 75 45 23

# input() : 한 줄의 문자열을 입력받는 함수
# map()   : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 예시 : 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용합니다.
#   list(map(int, input().split()))

# 예시 : 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용합니다
#   a,b,c = map(int, input().split())

#데이터의 개수 입력
#n = int(input())

#각 데이터를 공백을 기준으로 구분하여 입력 split()
#data = list(map(int, input().split())) #많이 사용되는 형태!!
#data.sort(reverse=True)
print(data)

#a,b,c = map(int, input().split())
#print(a,b,c)

#빠르게 입력 받기
# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 매서드 이용
#   단, 입력 후에 엔터가 줄바꿈 기호가 되므로 rstrip() 메서드를 함게 사용

import sys

#문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)


