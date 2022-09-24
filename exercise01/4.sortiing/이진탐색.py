def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if target == array[mid]:
        return mid

    if target < array[mid]:
        return binary_search(array, target, start, mid-1)

    else:
        return binary_search(array, target, mid+1, end)


n, target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result)