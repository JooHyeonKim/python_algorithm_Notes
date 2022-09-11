# 모험가 N명
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여
# 여행을 떠날 수 있는 그룹 수의 최댓값
# ex. N = 5
# 2 3 1 2 2
# {2,3,1}, {2,2} 2개 그룹
# 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.
#입력예시
#5
# 2 3 1 2 2
#출력예시
# 2

n = int(input())
array = list(map(int, input().split()))
array.sort() # 1 2 2 2 3
result = 0 # 총 그룹의 수
count = 0  # 현재 그룹에 포함되어 있는 모험가 수

for i in array:
    count +=1 # 현재 모험가를 현재 그룹에 포함
    # print('i:',i, ', result: ', result, ', count: ', count)
    if count >= i:
       result += 1  # 현재 모험가를 현재 그룹에 추가
       count = 0 # 현재 그룹에 포함된 모험가 수 초기화
print(result)



