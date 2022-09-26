t = int(input())  #t : testcase

for _ in range(t):
    n, m = map(int, input().split())  # n, m
    array = list(map(int, input().split()))

    dp = [] # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    index = 0

    for i in range(n):
        dp.append(array[index:m+index])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] += max(dp[i][j - 1], dp[i + 1][j - 1])
            if i == n-1:
                dp[i][j] += max(dp[i-1][j - 1], dp[i][j - 1])
            if 1 <= i < n-1:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

    # for i in range(n):
    #     for j in range(m):
    #         print(dp[i][j], end=' ')
    #     print()
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)




