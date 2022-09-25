from collections import deque

#공백을 기준으로 n과 m을 각각 입력받음
n, m = map(int,input().split())


#지도를 2차원 배열로 입력받음
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 다음 위치( 상 하 좌 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs로 최단경로 탐색
def dfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(dfs(0,0))
print(graph)