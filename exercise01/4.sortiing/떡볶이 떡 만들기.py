n, m = map(int, input().split())

def binary_search(array,m,start,end):

    mid = (start+end)//2
    if start > end:
        return mid

    print('(', start , end ,') mid: ', mid, end=' ')

    leftover = 0
    for i in range(n):
        if array[i] > mid:
            leftover += (array[i]-mid)

    print('leftover: ',leftover)

    if leftover == m:
        return mid
    if leftover < m:
        return binary_search(array,m,start,mid-1)
    else:
        return binary_search(array,m,mid+1,end)


array = list(map(int, input().split()))
end = max(array)

result = binary_search(array,m,0,end)

print(result)