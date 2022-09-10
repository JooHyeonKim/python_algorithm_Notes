list = input()
result = int(list[0])

for i in range(1,len(list)):
    num = int(list[i])
    if num <=1  or result<=1: #두 수 중에서 하나라도 0 혹은 1인 경우 곱하기보다는 더하기 수행
        result += num
    else:
        result *= num


print(result)

