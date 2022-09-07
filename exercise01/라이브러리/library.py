#실전에서 유용한 표준 라이브러리
#내장함수 : 기본 입출력함수부터 정렬 함수까지 기본적인 함수들 제공
# intertools
# 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 기능 제공
# 특히 순열과 조합 라이브러리는 코딩테스트에서 자주 사용됨

#heapq : heap 자료구조 제공
# 일반적으로 우선순위 큐 기능을 구현하기 위해 사용됨

#bisect : 이진탐색 기능 제공

# collections :
# deque, counter 등의 유용한 자료구조 포함

#math
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함

# sum()
result = sum([1,2,3,4,5])
print(result)

# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

# eval()
# 수 형태로 반환
result = eval("(3+5)*7")
print(result)


#sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)

#sorted() with key
array = [('홍길동',35), ('이순신',75), ('아무개',50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

#순열
#서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# {'A','B','C'}에서 두 개를 선택하여 나열하는 경우
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
from itertools import permutations #itertools에 정의되어 있는 permutations 라이브러리 활용
data = ['A','B','C'] #데이터 준비
result = list(permutations(data,2)) #모든 순열 구하기
print(result)


#조합
#서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# {'A', 'B', 'C'}에서 순서를 고려하지 않고 두개를 뽑는 경우

from itertools import combinations
data = ['A','B','C'] #데이터 준비
result = list(combinations(data,2))
print(result)

#중복순열
from itertools import product
data = ['A','B','C']
result = list(product(data, repeat=2))
print(result)
