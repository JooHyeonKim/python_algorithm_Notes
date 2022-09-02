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
