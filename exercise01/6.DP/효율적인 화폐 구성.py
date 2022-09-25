#입력예시1
#2 5, n=3, m=7
#2
#3
#출력예시1 > 5

#입력예시2
#3 4 n=3, m=4
#3
#5
#7
#출력예시 2 > -1 불가능할때는 -1 출력

n, m = map(int, input().split())
coin = [0]*n #화폐종류 저장

for i in range(n):
    coin[i] = int(input())

d = [10001]*(m+1)
#d[i] = 합이 i원이 되도록 하는 화폐의 최소 개수
d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if d[j - coin[i]] != 1001:
            d[j] = min(d[j], d[j - coin[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

#쉽지않았다...

