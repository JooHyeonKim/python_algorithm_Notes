from bisect import bisect_left, bisect_right

def count_by_bisect(array, target):
    left_index = bisect_left(array,target)
    right_index = bisect_right(array,target)
    return right_index - left_index

n, target = map(int, input().split())
array = list(map(int,input().split()))
result = count_by_bisect(array,target)

#print('result : ',result)
if result == 0:
    print(-1)
else:
    print(result)