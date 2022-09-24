n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:

        #해당 노드를 아직 방문하지 않았다면
        graph[x][y] = 1

        # 방문목적 dfs
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        #현재 위치에서 처음 dfs가 수행된 것 -> result +=1
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):

        # 이번 dfs를 통해 방문처리가 된거라면
        if dfs(i,j) == True:
            result += 1

print(result)

#계수 정렬 소스코드
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0]*(max(array)+1)

for k in array:
    count[k] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)



