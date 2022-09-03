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
