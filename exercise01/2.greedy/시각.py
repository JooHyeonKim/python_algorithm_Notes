#N
n = int(input())

# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
           if '3' in str(i) or '3' in str(j) or '3' in str(k):
               #print(i,j,k)
               cnt+=1

print(cnt)

#이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제이다.
# 전형적인 완전탐색(Brute Forcing)이자 구현문제
# 완전 탐색 : 가능한 경우의 수를 모드 검사해보는 탐색방법
