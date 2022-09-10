# n, k = map(int, input().split())
#
# while n!=1:
#     if n%k == 0:
#         n = n//k
#         cnt += 1
#         print(n)
#     else:
#         n-=1
#         cnt += 1
#         print(n)
#
# print(cnt)
#양재주현 풀이

n, k = map(int, input().split())
result = 0

while True:

    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k
    result +=(n - target)
    n = target

    #N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break

    #k로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기

result += (n-1)
print(result)

