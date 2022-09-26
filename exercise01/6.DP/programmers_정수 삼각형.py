triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

n = len(triangle)

for i in range(n):

    for j in range(len(triangle[i])):
        if j == 0 and i == 0:
            continue
        if j == 0 and i >= 1:
            triangle[i][j] += triangle[i - 1][j]
            continue
        if i == j:
            triangle[i][j] += triangle[i - 1][j - 1]
            continue
        if 1 <= i <= n - 1 and 1 <= j < i:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

answer = 0

for i in range(n):
    for j in range(len(triangle[i])):
        print(triangle[i][j], end = ' ')
    print()

for k in range(n):
    answer = max(answer, triangle[n - 1][k])

print(answer)