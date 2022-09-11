# # (1,1)(1,2)(1,3)
# # (2,1)(2,2)(2,3)
# # (3,1)(3,2)(3,3)
#
# #     동 북 서 남
# #     R U L  D
# dx = [0,-1,0,1]
# dy = [1,0,-1,0]
#
# n = int(input()) #공간의 크기 1<= n <=100
# direct = input().split()
# # ['R', 'R', 'R', 'U', 'D', 'D']
# print(direct)
#
# x,y=1,1 #실제 이동위치
# nx, ny = 0,0 #임시저장 다음위치
# for d in direct:
#     if d=='R':
#         nx = x + dx[0]
#         ny = y + dy[0]
#
#     if d=='U':
#         nx = x + dx[1]
#         ny = y + dy[1]
#
#     if d=='L':
#         nx = x + dx[2]
#         ny = y + dy[2]
#
#     if d=='D':
#         nx = x + dx[3]
#         ny = y + dy[3]
#
#     if 1<=nx<=n and 1<=ny<=n: #이동한 위치가 지도를 벗어나지 않는 경우
#         x=nx
#         y=ny
#
#     else: #이동한 위치가 지도를 벗어난 경우. 이동안함
#         nx=x
#         ny=y
#
#     print(x,',',y,'로 이동')
#
# print('도착위치 : ',x,y)
#양재주현 풀이

#N 입력받기
n = int(input())
x,y = 1,1
plans = input().split()
# L R U D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인하기
for plan in plans:

    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plans == move_types[i]:
            nx = x + x[i]
            ny = y + y[i]

    #공간을 벗어나는 경우 무시
    if nx<1 or nx>n or ny<1 or ny>n:
        continue #아래 코드 실행 안하고 반복문으로

    #이동 수행
    x,y = nx, ny
    print(x,y ,'로 이동')

print()


