# N : 식량창고의 개수
# 공백을 기준으로 각 식량창고에 저장된 식량의 개수 K가 주어짐.

#입력예시
# 4
# 1 3 1 5

N = int(input())
food = list(map(int, input().split()))
dp = [0]*N

dp[0] = food[0]
dp[1] = max(food[0],food[1])

for i in range(N):
    dp[i] = max(dp[i - 1], dp[i - 2] + food[i])

print(dp[N-1])