n = int(input())

array = list(map(int, input().split()))

d = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[i]