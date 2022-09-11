#     동 북 서 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#현재위치
x, y = 2, 2

#다음 위치 동북서남 순서로 다음 위치 보여줌
for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    print(nx, ny)
