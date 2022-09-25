#한 번 계산된 결과를 메모이제이션

d = [0]*100

def fibbo(x):
    print('fibbo(',x,')')
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    else:
        d[x] = fibbo(x-1) + fibbo(x-2)
        return d[x]

print(fibbo(6))